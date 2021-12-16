WÖrterbücher





adb shell 'pm list packages -f'
for i in $(adb shell pm list packages -3 | awk -F':' '{print $2}'); do echo $i >> packages.txt; done

//copz via MTP



https://wiki.lineageos.org/devices/klte

wget https://mirrorbits.lineageos.org/full/klte/20211031/lineage-18.1-20211031-nightly-klte-signed.zip

manually copy the files from the SD card

to install twrp for the first time
adb reboot download
heimdall flash --RECOVERY ~/Downloads/twrp-3.3.1-0-klte.img  --no-reboot

wget https://eu.dl.twrp.me/klte/twrp-3.5.2_9-0-klte.img --output-document=$HOME/Downloads/twrp-3.5.2_9-0-klte.img
wget https://f-droid.org/FDroid.apk --output-document=$HOME/Downloads/FDroid.apk


adb reboot recovery
adb shell twrp wipe dalvik && adb shell twrp wipe cache && adb shell twrp wipe data

adb shell twrp sideload && sleep 5 && adb sideload ~/Downloads/lineage-18.1-20211031-nightly-klte-signed.zip

adb shell twrp sideload && sleep 5 && adb sideload ~/Downloads/MindTheGapps-11.0.0-arm-20210920_083829.zip

adb shell twrp sideload && sleep 5 && adb sideload ~/Downloads/Magisk-v23.0.apk


// developer options

maybe repeat 
adb shell twrp sideload && sleep 5 && adb sideload ~/Downloads/Magisk-v23.0.apk


https://github.com/YTVanced/VancedManager/releases/download/v2.5.0/manager.apk
 adb install ~/Downloads/manager.apk 

adb install ~/Downloads/FDroid.apk
adb install ~/Downloads/MagiskManager-v7.5.1.apk



Notfallinformationen 
