terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
    }
  }
}

variable "project_id" {}
variable "region" {}
variable "zone" {}

locals {
  feature_store = {
    name = "example"
    entity_types = toset([
      "movie", "user"
    ])
    fixed_node_count = 1
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}
