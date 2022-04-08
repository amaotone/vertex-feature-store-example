resource "google_vertex_ai_featurestore" "featurestore" {
  provider = google-beta
  name     = local.feature_store.name

  online_serving_config {
    fixed_node_count = local.feature_store.fixed_node_count
  }
}

resource "google_vertex_ai_featurestore_entitytype" "entity" {
  provider     = google-beta
  for_each     = local.feature_store.entity_types
  name         = each.value
  featurestore = google_vertex_ai_featurestore.featurestore.id
}
