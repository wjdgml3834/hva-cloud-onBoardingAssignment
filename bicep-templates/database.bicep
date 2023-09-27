param location string
param sqlServerName string
param sqlDatabaseName string
param sqlAdminLogin string
@secure()
param sqlAdminPassword string 
param startIpAddress string 
param endIpAddress string 

resource sqlServer 'Microsoft.Sql/servers@2021-02-01-preview' = {
  name: sqlServerName
  location: location
  properties: {
    version: '12.0'
    administratorLogin: sqlAdminLogin
    administratorLoginPassword: sqlAdminPassword
  }
}

resource sqlDatabase 'Microsoft.Sql/servers/databases@2021-02-01-preview' = {
  name: sqlDatabaseName
  location: location
  parent: sqlServer 
  properties: {
    collation: 'SQL_Latin1_General_CP1_CI_AS'
    maxSizeBytes: 1073741824
    readScale: 'Disabled'
    zoneRedundant: false
  }
}

resource sqlFirewallRule 'Microsoft.Sql/servers/firewallRules@2021-02-01-preview' = {
  name: 'AllowSpecificIPRange'
  parent: sqlServer
  properties: {
    startIpAddress: startIpAddress
    endIpAddress: endIpAddress
  }
}
