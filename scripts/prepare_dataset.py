from pathlib import Path

import fire
import pandas as pd


def create_feature_csv():
    root_dir = Path(__file__).parent.parent
    input_dir = root_dir / "data/ml-1m"
    output_dir = root_dir / "data/features"

    # users
    print("users")
    users = pd.read_csv(
        input_dir / "users.dat",
        sep="::",
        header=None,
        engine="python",
        encoding="iso-8859-1",
    )
    users.columns = ["user_id", "gender", "age", "occupation", "zip_code"]

    # movies
    print("movies")
    movies = pd.read_csv(
        input_dir / "movies.dat",
        sep="::",
        header=None,
        engine="python",
        encoding="iso-8859-1",
    )
    movies.columns = ["movie_id", "title", "genre"]

    # ratings
    print("ratings")
    ratings = pd.read_csv(
        input_dir / "ratings.dat",
        sep="::",
        header=None,
        engine="python",
        encoding="iso-8859-1",
    )
    ratings.columns = ["user_id", "movie_id", "rating", "timestamp"]
    ratings["timestamp"] = pd.to_datetime(ratings.timestamp, unit="s")

    timestamps = [
        pd.to_datetime("2000-10-01"),
        pd.to_datetime("2000-11-01"),
        pd.to_datetime("2000-12-01"),
    ]
    for ts in timestamps:
        df = ratings.query("timestamp < @ts")
        user_feat = df.groupby("user_id").agg(
            {
                "movie_id": "count",
                "rating": "mean",
            }
        )
        user_feat.columns = ["review_count", "average_rating"]
        user_feat = users.merge(
            user_feat, how="right", left_on="user_id", right_index=True
        )
        user_feat["timestamp"] = ts.isoformat()

        movie_feat = df.groupby("movie_id").agg(
            {
                "user_id": "count",
                "rating": "mean",
            }
        )
        movie_feat.columns = ["review_count", "average_rating"]
        movie_feat = movies.merge(
            movie_feat, how="right", left_on="movie_id", right_index=True
        )
        movie_feat["timestamp"] = ts.isoformat()

        print(ts.date())
        user_feat.to_csv(output_dir / f"user_feat_{ts.date()}.csv", index=False)
        movie_feat.to_csv(output_dir / f"movie_feat_{ts.date()}.csv", index=False)


if __name__ == "__main__":
    fire.Fire(create_feature_csv)
