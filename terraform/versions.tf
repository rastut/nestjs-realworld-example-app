terraform {
  required_version = "1.0.7"  
  required_providers {
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 3.84.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 3.84.0"
    }
  }
}


