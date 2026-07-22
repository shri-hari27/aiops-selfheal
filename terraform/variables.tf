variable "resource_group_name" {
  description = "Azure Resource Group name"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
}

variable "app_service_plan_name" {
  description = "App Service Plan name"
  type        = string
}

variable "web_app_name" {
  description = "Linux Web App name"
  type        = string
}

variable "docker_image" {
  description = "Docker image"
  type        = string
}

variable "docker_tag" {
  description = "Docker image tag"
  type        = string
}
