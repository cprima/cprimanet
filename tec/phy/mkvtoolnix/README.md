---
component: TA_PTC_025
---

```
Get-ChildItem . -Filter *2021-05-27*.mkv | Foreach-Object { echo $_ ; D:\opt\MKVToolNix\mkvpropedit.exe $_  --edit info --set "title=tec phy CHDK timelapse script download and copy" }
```