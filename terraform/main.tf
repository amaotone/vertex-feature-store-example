terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

variable "project_id" {}

provider "google" {
  project = var.project_id
  region  = "asia-northeast1"
  zone    = "asia-northeast1-c"
}

provider "google-beta" {
  project = var.project_id
  region  = "asia-northeast1"
  zone    = "asia-northeast1-c"
}

resource "google_vertex_ai_featurestore" "featurestore" {
  provider = google-beta
  name     = "example_feature_store"

  online_serving_config {
    fixed_node_count = 0
  }
}
