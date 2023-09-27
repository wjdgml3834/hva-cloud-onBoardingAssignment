targetScope = 'subscription'

param rgName string = 'onBoardingResourceGroup' 
param location string = 'westeurope' 
param sqlServerName string = 'HvaOnBoardingSQLServer'
param sqlDatabaseName string = 'onBoardingDatabase'
param sqlAdminLogin string
@secure()
param sqlAdminPassword string 
param startIpAddress string = '0.0.0.0' 
param endIpAddress string = '255.255.255.255'


// 리소스 그룹 모듈 호출
module resourceGroupModule 'resource-group.bicep' = {
  name: 'resourceGroupDeployment'
  params: {
    rgName: rgName
    location: location
  }
}

// 데이터베이스 모듈 호출
module database 'database.bicep' = {
  name: 'databaseModule'
  scope: resourceGroup(rgName) // 이 부분이 중요합니다. 이를 통해 해당 리소스 그룹에 배포됩니다.
  params: {
    location: location
    sqlServerName: sqlServerName
    sqlDatabaseName: sqlDatabaseName
    sqlAdminLogin: sqlAdminLogin
    sqlAdminPassword: sqlAdminPassword
    startIpAddress: startIpAddress
    endIpAddress: endIpAddress
  }
  dependsOn: [
    resourceGroupModule // 리소스 그룹이 먼저 생성되어야 합니다.
  ]
}












