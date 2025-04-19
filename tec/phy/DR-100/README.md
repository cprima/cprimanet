---
component: TA_PTC_025
---

```
Get-ChildItem . -Filter *.wav | Foreach-Object { $_.CreationTime=$(Get-Date -format o); $_.LastWriteTime=$(Get-Date -format o) }
```