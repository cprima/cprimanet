---
layout: post
title: Use Companion to mute MS Teams
component: TA_PTC_002
date:   2021-04-28 12:00:00 +0100
abstract: "Finally found a readable way to toggle the mute status in MS Teams."
---


Finally found a readable way to toggle the mute status in MS Teams:

With an action "internal: Run shell path (local)" I use

```%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe "$procid = Get-Process | Where-Object { $_.MainWindowTitle -like '*Microsoft Teams*' }  | Select-Object Id | select -Expand Id;  $wshell = New-Object -ComObject wscript.shell; $wshell.AppActivate($procid); Sleep 1; $wshell.SendKeys('^+m'); $wshell.SendKeys('%+{TAB}');"```

(MS Teams only accepts keystrokes/shortcuts with focus on (one of) its window)

[Companion User Group posting](https://www.facebook.com/groups/companion/permalink/2853525641532434/?__cft__[0]=AZUo4q8u6xNKu5teCy3hLASFMNdRLaqZWHFysMpzgjD046FwXZrOtRAVGlw0XcDiTmYTTlmmQ3kOj4G-wPx3TBHCgcaiAxqlmKoby-cAanjFVaiIJTxe4-lvPZAes-2koVI&__tn__=%2CO%2CP-R)
