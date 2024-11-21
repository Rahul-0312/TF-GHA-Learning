terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.10.0"
    }
  }
}

provider "azurerm" {
    features {}
    subscription_id = "51dda057-fda7-4265-acf8-945f0d0fcebd"
}