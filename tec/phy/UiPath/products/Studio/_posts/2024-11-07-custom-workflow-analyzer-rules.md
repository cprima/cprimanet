---
---

## Prequisites

https://docs.uipath.com/sdk/other/latest/developer-guide/creating-activities-with-code

```
choco install visualstudio2022community --package-parameters "--add Microsoft.VisualStudio.Workload.ManagedDesktop --add Microsoft.VisualStudio.Workload.NetWeb --add Microsoft.VisualStudio.Workload.VisualStudioExtension"
choco install dotnet-6.0-sdk
choco install dotnet-6.0-runtime
choco install nuget.commandline
```

Development Settings: Visual C# or General Development

official feed

https://github.com/UiPath/Community.Activities/tree/develop/Activities/Templates/UiPath.Activities.Template/VisualStudio

https://docs.uipath.com/sdk/other/latest/developer-guide/building-workflow-analyzer-rules

> When building custom rules, target the .NET version depending on the version of Studio and the project compatibility:
>
> Studio 2021.4 and earlier: .NET Framework 4.6.1.
> Studio 2021.10.6 and later: .NET Framework 4.6.1 for Windows-legacy projects, .NET 6 for Windows and cross-platform projects.

### Validate

`dotnet --list-sdks`

## Decisions

targetFramework: Windows only?

## solutions

Class Library (.NET Framework)
C#
Windows
.NET 6.0
