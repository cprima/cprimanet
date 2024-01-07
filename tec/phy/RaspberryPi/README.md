https://jamesachambers.com/raspberry-pi-4-usb-boot-config-guide-for-ssd-flash-drives/

ntfs on linux

sudo apt-get install ntfs-3g

push-button shutdown

/boot/config.txt
dtoverlay=gpio-shutdown
enable_uart=1
