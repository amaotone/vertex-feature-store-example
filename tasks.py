import invoke


@invoke.task
def download_dataset(c):
    url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
    c.run(f"wget {url} -O ./data/ml-1m.zip")
    c.run(f"unzip -o ./data/ml-1m.zip -d data")
