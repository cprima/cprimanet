---

---


{% include checklist.html checklistnames="Update Android" heading="h3" %}


useful commands:

```
adb reboot recovery
adb shell svc usb setFunctions mtp
```


/data/system/users/0/wallpaper is the current png wallpaper

CPM: klte, armeabi-v7a
CPM2: kltedv
AM:

https://mirrorbits.lineageos.org/full/klte/20230227/lineage-18.1-20230227-nightly-klte-signed.zip


```
adb reboot recovery
adb shell twrp wipe dalvik
adb shell twrp wipe cache
adb shell twrp wipe data
#adb shell twrp wipe system
adb shell twrp sideload && sleep 5 && adb sideload lineage-18.1-20230227-nightly-klte-signed.zip
adb shell twrp sideload && sleep 5 && adb sideload MindTheGapps-11.0.0-arm-20220217_095902.zip
adb shell twrp sideload && sleep 5 && adb sideload Magisk-v25.2.apk
adb install -r F-Droid.apk
adb shell twrp sideload && sleep 5 && adb sideload Telegram.apk
adb shell twrp reboot
```


cp /storage/emulated/0/Android/data/menion.android.locus.pro/files/Locus/backup/2023-03-19_09-38-57.zip /mnt/sdcard/Documents/
cp /sdcard/Android/data/dev.ukanth.ufirewall.donate/files/afwall-backup-all-2023-03-19-09-45-06.json


AFWall Export

Locus Classic: https://drive.google.com/drive/folders/1Dk5GUNiKq11EdnT3Q5AIFrhIGbxqyBsz Afa!!! - Classic Google Play, AFA - Google Play version with one addition > "All files access" - useful for Android 11+ devices to have full file access and also possibility to move app root directory to the root of internal memory.

PlayStore:
Finanzassistent
IBKR
Jota+
Magic Earth
Post&DHL
Raumfeld
Messenger Lite
Forumslader
AFWall
QRControl


direct download:
Telegram
Locus Classic https://drive.google.com/drive/folders/1Dk5GUNiKq11EdnT3Q5AIFrhIGbxqyBsz
Signal https://signal.org/android/apk/
Magisk
Vanced Manager https://d.vancedmanager.com/VancedManager_v2.6.2.apk

F-Droid:
QR & Barcode scanner
Syncthing
brouter
ConnectBot
KeePass DX
Hackers Keyboard
CPU Info

apkmirror:
Chrome Canary
Droid Hardware Info 1.2.3

datadir
Brouter: external SD card

todo:
- Authy
- K9

