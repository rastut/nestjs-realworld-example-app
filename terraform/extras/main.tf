provider "google" {
  project = var.project
}

resource "google_container_registry" "nestjs-realworld-registry" {
  project  = "useful-tempest-624"
  location = "EU"
}

resource "google_storage_bucket_iam_member" "viewer" {
  bucket = google_container_registry.nestjs-realworld-registry.id
  role = "roles/storage.objectViewer"
  member = "user:${var.user}"
}
