---
---

sudo salt 'node03' cmd.run "net use Z: \\\\edge\\share & dir Z: & choco install uipathstudiocommunity -y --source 'Z:\choco\packages' --install-arguments=\"'ADDLOCAL=DesktopFeature,Studio,Robot,ExcelAddin,ChromeExtension,EdgeExtension ORCHESTRATOR_URL=\"https://cloud.uipath.com/\" ORCHESTRATOR_AUTO_SIGNIN='0' CUSTOM_NUGET_FEEDS=\"project-basturma-packages,https://www.myget.org/F/project-basturma-packages/api/v3/index.json\" ENABLE_PIP=1 TELEMETRY_ENABLED=0'\" --force --no-progress"

CommunityEdition:
RegisterService will not allow to login to Orchestrator with e.g. URL and machinekey

sudo salt 'node03' cmd.run "net use Z: \\\\edge\\share & dir Z: & choco install uipathstudiocommunity -y --source 'Z:\choco\packages' --install-arguments=\"'ADDLOCAL=DesktopFeature,Studio,Robot,ExcelAddin,ChromeExtension,EdgeExtension ORCHESTRATOR_URL=\"https://cloud.uipath.com/\" ORCHESTRATOR_AUTO_SIGNIN='0' CUSTOM_NUGET_FEEDS=\"project-basturma-packages,https://www.myget.org/F/project-basturma-packages/api/v3/index.json\" ENABLE_PIP=1 TELEMETRY_ENABLED=0'\" --force --no-progress"
