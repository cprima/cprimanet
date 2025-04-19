


https://sketchviz.com/@cprima/f7350250e107219fef20e94fdb7e5df5/26d059a8024278f9d350ff5a2e30b258e6647033

https://forum.fairphone.com/t/newbie-fairphone-os-too-bloated-for-my-taste-need-your-tipps/99027/4


https://code.fairphone.com/projects/fairphone-4/kernel.html


storage
factory reset: system 21 GB


2023-08-21
Build number FP4.SP2J.B.086.20230729


architecture: armXXXXXXXXXXXX?
bit:



C:\Users\cpm>adb reboot fastboot

C:\Users\cpm>O:

O:\>cd O:\platform-tools

O:\platform-tools>fastboot.exe flashing unlock
< waiting for any device >
^C
O:\platform-tools>adb.exe devices
adb server version (39) doesn't match this client (41); killing...
* daemon started successfully
List of devices attached
fd56a3ec        device


O:\platform-tools>adb.exe reboot bootloader

O:\platform-tools>fastboot.exe devices

O:\platform-tools>fastboot.exe devices
fd56a3ec         fastboot

O:\platform-tools>fastboot.exe flashing unlock
OKAY [  0.035s]
Finished. Total time: 0.038s

O:\platform-tools>


> TWRP
> Fairphone does not support the use of the TWRP (Team Win Recovery Project), as it might cause malfunctioning.
> https://support.fairphone.com/hc/en-us/articles/10492476238865-Manage-the-Bootloader