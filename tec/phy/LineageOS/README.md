---
checklists: []
---

- Bootloader
- ROM


# Prerequisites

For the bootloader: `choco install heimdall`or https://glassechidna.com.au/heimdall/#downloads

For the ROM: adb `choco install android-sdk` or https://developer.android.com/tools/releases/platform-tools


{% include checklist.html checklistnames="Update Android" heading="h3" %}


## status 2024-06

LineageOS stopped building Samsung Galaxy S5 and their downloads do ot contain archives.
Serves as a reminder to fully investigate and download all resources before updates are attempted.

An unofficial archive is available at https://lineage-archive.timschumi.net/

In the forums XDA unofficial builds of LineageOS 20 (Android 13) and LineageOS 21 can be found at https://xdaforums.com/t/unofficial-lineageos-20-0-android-13.4498857/


### Samsung S5

- klte: latest nightly build was lineage-18.1-20240306-nightly-klte-signed.zip
- kltedv

## Bootloader TWRP

- klte: https://twrp.me/samsung/samsunggalaxys5qualcomm.html
- kledv:


### update TWRP Samsung S5

1. download https://eu.dl.twrp.me/klte/twrp-3.7.0_9-0-klte.img from 
1. adb push /sdcard/
1. adb reboot recovery
1. install ("img"!) and swipe

### install TWRP SAmsung S5

to install twrp for the first time
adb reboot download
heimdall flash --RECOVERY ~/Downloads/twrp-3.3.1-0-klte.img  --no-reboot

wget https://eu.dl.twrp.me/klte/twrp-3.5.2_9-0-klte.img --output-document=$HOME/Downloads/twrp-3.5.2_9-0-klte.img

## LineageOS 18

```
adb reboot recovery
adb shell twrp wipe dalvik
adb shell twrp wipe cache
adb shell twrp wipe data
#adb shell twrp wipe system
adb shell twrp sideload && sleep 5 && adb sideload lineage-18.1-20240306-nightly-klte-signed.zip
adb shell twrp sideload && sleep 5 && adb sideload MindTheGapps-11.0.0-arm-20230922_081034.zip
#adb install -r F-Droid.apk
adb shell twrp reboot
```

## LineageOS 20 / Anddroid 13

https://xdaforums.com/t/unofficial-lineageos-20-0-android-13.4498857/

https://xdaforums.com/t/mod-flashable-microg-unofficial-installer.3432360/

```
adb sideload lineage-20.0-20240927-UNOFFICIAL-klte.zip
adb sideload MindTheGapps-13.0.0-arm-20231025_200806.zip
```

## MindTheGapps vs. microg

todo

