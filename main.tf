resource "azurerm_resource_group" "gotham_rg" {
  name     = "gotham_resource_group"
  location = "centralindia"
}

resource "azurerm_storage_account" "example" {
  name                     = "GothamDepot"
  resource_group_name      = azurerm_resource_group.gotham_rg.name
  location                 = azurerm_resource_group.gotham_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    belongs_to = "gotham_police_dept"
  }
}