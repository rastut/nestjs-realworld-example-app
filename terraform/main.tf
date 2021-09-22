provider "google-beta" {
  project = var.project
}
data "google_project" "project" {
  provider = google-beta
}

#Creates a secret storage for nestjs DB 
resource "google_secret_manager_secret" "dbnestjs_password" {

  secret_id = var.secret_id
  
  replication {
    automatic = true
  }
}

resource "google_secret_manager_secret_version" "secret-version-data" {
  secret = google_secret_manager_secret.dbnestjs_password.name
  # On a real environment I will never push a plain text password.
  # The ideal is have some secret storage as Vault, and use a data provider
  # to get the secret or have some kind of encryption via KMS. This is only
  # for the porpuse of this task.
  secret_data = var.db_password
}

#Grants access to the default service account used by Cloud Run
resource "google_secret_manager_secret_iam_member" "dbnestjs_password_access" {
  secret_id = google_secret_manager_secret.dbnestjs_password.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com"
  depends_on = [google_secret_manager_secret.dbnestjs_password]
}

# Creates Postgresql db 
resource "google_sql_database_instance" "postgres_nestjs" {
  name             = var.cloudsql_instance_name
  database_version = var.cloudsql_instance_version
  region           = var.region

  settings {

    #tier = "db-custom-2-7680"
    tier = var.cloudsql_instance_tier
    availability_type = var.cloudsql_instance_availabitlity
    disk_size = var.cloudsql_instance_disk_size
    
    database_flags {
      name = "cloudsql.iam_authentication"
      value = "on"
    }

    backup_configuration {
      enabled = true
      point_in_time_recovery_enabled = true 
    }

    maintenance_window {
      day = 1
      hour = 2
      update_track = "stable"
    }
  }

  deletion_protection = true
  
}

#Creates the SQL database in the SQL instance
resource "google_sql_database" "database" {
  name     = var.db_name
  instance = google_sql_database_instance.postgres_nestjs.name

  depends_on = [google_sql_database_instance.postgres_nestjs]
}

# Password-less user. Granting permissions through IAM and not Built-In. This should avoid the password. Not tested
resource "google_sql_user" "compute_svc_access" {
  name     = "${data.google_project.project.number}-compute@developer.gserviceaccount.com"
  instance = google_sql_database_instance.postgres_nestjs.name
  type     = "CLOUD_IAM_USER"

  depends_on = [google_sql_database_instance.postgres_nestjs]
}

# Creates Cloud Run Service for the application. Includes the prod configuration
resource "google_cloud_run_service" "nestjsrealworld" {
  provider = google-beta
  name     = var.cloudrun_name
  location = var.region

  template {
    spec {
      containers {
        image = var.image
        ports {
          container_port = 3000
        }
        command = [ "npm", "run", "start:prod" ]
        env {
          name = "TYPEORM_PASSWORD"
          value_from {
            secret_key_ref {
              name = google_secret_manager_secret.dbnestjs_password.secret_id
              key = "1"
            }
          }
        }
        env {
          name = "TYPEORM_CONNECTION"
          value = var.typeorm_connection
        }
        env {
          name = "TYPEORM_HOST"
          value = "${google_sql_database_instance.postgres_nestjs.public_ip_address}"
        }
        env {
          name = "TYPEORM_USERNAME"
          value = var.db_username
        }
        env {
          name = "TYPEORM_DATABASE"
          value = var.db_name
        }
        env {
          name = "TYPEORM_PORT"
          value = var.db_port
        }
        env {
          name = "TYPEORM_LOGGING"
          value = var.typeorm_logging
        }
        env {
          name = "TYPEORM_ENTITIES"
          value = var.typeorm_entities
        }                      
      }
    }
  }

  metadata {
    annotations = {
      generated-by = "terraform"
      maintained-by = var.maintainers
      team = var.team
      "run.googleapis.com/launch-stage" = "BETA"
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  autogenerate_revision_name = true

  lifecycle {
    ignore_changes = [
        metadata.0.annotations,
    ]
  }

  depends_on = [google_secret_manager_secret_version.secret-version-data, google_sql_database_instance.postgres_nestjs]
}

resource "google_cloud_run_domain_mapping" "domain_netjs" {
  location = var.region
  name     = var.cloudrun_domain

  metadata {
    namespace = data.google_project.project.number
  }

  spec {
    route_name = google_cloud_run_service.nestjsrealworld.name
  }

  depends_on = [
    google_cloud_run_service.nestjsrealworld
  ]
}