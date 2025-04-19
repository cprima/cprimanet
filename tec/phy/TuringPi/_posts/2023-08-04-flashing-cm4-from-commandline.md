---
layout: post
title: Flashing a Raspberry Pi Compute Module 4 from the command line
component: TA_PTC_051
date:   2023-08-04 12:00:00 +0100
abstract: "A plain sequence of commands that were tested in 2023-08 to work on a TuringPi 2 with BMC version 1.1.0"
---


## Flashing a Raspberry Pi Compute Module 4 from the command line

Here a plain sequence of commands that were tested in 2023-08 to work on a TuringPi 2 with BMC version 1.1.0

````bash
ssh root@turingpi.local #turing
tpi -n 1 -l -f /mnt/sdcard/images/2023-05-03-raspios-bullseye-armhf-lite.img
tpi -n 1 -m
mount /dev/sda1 /mnt/bootfs
vi /mnt/bootfs/config.txt #enable_uart=1 in a section [all]
touch /mnt/bootfs/ssh
echo 'pi:$6$c70VpvPsVNCG0YR5$l5vWWLsLko9Kj65gcQ8qvMkuOoRkEagI90qi3F/Y7rm8eNYZHW8CY6BOIKwMH7a3YYzZYL90zf304cAHLFaZE0' > /mnt/bootfs/userconf
umount /mnt/bootfs
tpi -n 1 -x
tpi -u host -n 1
tpi -p off -n 1 && tpi -p on -n 1
watch -n 5 tpi --uart=get -n 1
ssh pi@raspberrypi
rm .ssh/known_hosts
ssh pi@raspberrypi
````