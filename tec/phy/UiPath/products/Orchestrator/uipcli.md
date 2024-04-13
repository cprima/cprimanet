---
title: UiPath uipcli.exe commands
---

UiPathCloudAccountName
UiPathCloudFolderName
UiPathCloudTenantName
UiPathCloudOrchestratorUrl
UiPathCloudAdminTenantServicesApiAccessKey
UiPathCloudApplicationId
UiPathCloudApplicationSecret
UiPathCloudApplicationScope

## Jobs

O:\UiPath.CLI.Windows\23.6.8581.19168\tools\uipcli.exe job run "BlankProcess" "https://cloud.uipath.com/" homelab23 --organizationUnit Shared --accountForApp cprimadotnet --applicationId "123e4567-e89b-12d3-a456-426655440000" --applicationSecret "Secret01234!@#$" --applicationScope "OR.Execution OR.Folders OR.Jobs OR.Settings" --result_path T:\uipcli-jobrun-result.json --traceLevel Verbose --jobscount 3 --wait False

$env:UiPathCloudAdminTenantServicesApiAccessKey = 'Admin#TenantServicesApiAccessKey'

O:\UiPath.CLI.Windows\23.6.8581.19168\tools\uipcli.exe job run "BlankProcess" "https://cloud.uipath.com/" "homelab23" --organizationUnit "Shared" --token $env:UiPathCloudAdminTenantServicesApiAccessKey --accountName "cprimadotnet" --result_path T:\uipcli-jobrun-result.json --traceLevel "Verbose" --jobscount 3 --wait False

## Packages

O:\UiPath.CLI.Windows\23.6.8581.19168\tools\uipcli.exe package pack "C:\Users\cpm\Documents\UiPath\BlankProcess\project.json" --output "T:\" --traceLevel Verbose --autoVersion --disableTelemetry --outputType Process

$env:UiPathCloudAdminTenantServicesApiAccessKey = 'Admin#TenantServicesApiAccessKey'
O:\UiPath.CLI.Windows\23.6.8581.19168\tools\uipcli.exe package deploy "T:\BlankProcess9.1.0.155849918.nupkg" "https://cloud.uipath.com/" "homelab23" --token $env:UiPathCloudAdminTenantServicesApiAccessKey --accountName "cprimadotnet"

O:\UiPath.CLI.Windows\23.6.8581.19168\tools\uipcli.exe package deploy "T:\BlankProcess9.1.0.155849918.nupkg" $env:UiPathCloudOrchestratorUrl $env:UiPathCloudFolderName --token $env:UiPathCloudAdminTenantServicesApiAccessKey --accountName $env:UiPathCloudAccountName

```powershell
# SetUiPathCloudEnvVars.ps1

<#
.SYNOPSIS
Sets environment variables for UiPath Cloud account, tenant, and orchestrator URL.

.DESCRIPTION
This script takes a UiPath Cloud URL as input and sets environment variables for the
account name, Sets environment variables for UiPath Cloud account, tenant, and orchestrator URL.
 name, and base orchestrator URL. It is useful for automating tasks
that require these values to be set as environment variables.

.PARAMETER url
The UiPath Cloud URL to parse.

.EXAMPLE
.\SetUiPathCloudEnvVars.ps1 -url "https://cloud.uipath.com/cprimadotnet/homelab23/orchestrator_/"
Sets the environment variables based on the provided UiPath Cloud URL.

.NOTES
Author: Christian Prior-Mamulyan
Date: 2023-12-10
#>

# Accepting the URL as a parameter
param (
    [string]$url
)

# Function to set environment variables based on the provided URL
function SetEnvironmentVariables($inputUrl) {
    # Splitting the URL into parts
    $urlParts = $inputUrl -split '/'

    # Extracting account name and Sets environment variables for UiPath Cloud account, tenant, and orchestrator URL.
 name from the URL
    # Assumes the URL format is https://cloud.uipath.com/{account}/{tenant}/orchestrator_/
    $accountName = $urlParts[3]
    $tenantName = $urlParts[4]
    # Constructing the base URL
    $orchestratorUrl = $urlParts[0] + '//' + $urlParts[2]

    # Setting the extracted values as environment variables
    $env:UiPathCloudAccountName = $accountName
    $env:UiPathCloudTenantName = $tenantName
    $env:UiPathCloudOrchestratorUrl = $orchestratorUrl

    # Displaying the set variables for confirmation
    Write-Host "UiPathCloudAccountName set to: $env:UiPathCloudAccountName"
    Write-Host "UiPathCloudTenantName set to: $env:UiPathCloudTenantName"
    Write-Host "UiPathCloudOrchestratorUrl set to: $env:UiPathCloudOrchestratorUrl"
}

# Executing the function with the provided URL
SetEnvironmentVariables $url


```
