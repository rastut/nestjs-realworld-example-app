variable "project" {
    type = string
    default = "useful-tempest-624"
}

variable "maintainers" {
    type = string
    default = "devops"
}

variable "team" {
    type = string
    default = "TemRocket"
}

variable "region" {
    type = string
    default = "europe-west1"
}

variable "image" {
    type = string
    default = "dockerimage:last"
}

variable "secret_id" {
    type = string
    default = "dbnestjs_postgres"
}

variable "db_password" {
    type = string
    default = "password"
}

variable "db_name" {
    type = string
    default = "nestjsrealworld"  
}

variable "db_username" {
    type = string
    default = "nestjsrealworld"  
}

variable "db_port" {
    type = string
    default = "5432"  
}

variable "typeorm_entities" {
    type = string
    default = "dst/**/**.entity.js"
}

variable "typeorm_logging" {
    type = string
    default = "true"
}

variable "typeorm_connection" {
    type = string
    default = "postgres"
}


variable "cloudsql_instance_name" {
    type = string
    default = "db_nestjsrealworld"
}

variable "cloudsql_instance_version" {
    type = string
    default = "POSTGRES_13"
}


variable "cloudsql_instance_availabitlity" {
    type = string
    default = "REGIONAL"
}

variable "cloudsql_instance_disk_size" {
    type = number
    default = 50
  
}

variable "cloudsql_instance_tier" {
    type = string
    default = "db-f1-micro"
}

variable "cloudrun_domain" {
    type = string
    default = "www.nestjsrealworld.com"
}
variable "cloudrun_name" {
    type = string
    default = "nestjs-realworld-example-app"
}