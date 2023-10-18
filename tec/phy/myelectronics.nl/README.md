https://www.myelectronics.nl/us/snap-in-momentary-push-button-switch-blue-led.html

/boot/config.txt
dtoverlay=gpio-shutdown
enable_uart=1

dtoverlay -h gpio-shutdown

sudo dtoverlay -l

https://dietpi.com/forum/t/dietpi-v6-28-0-rpi-zero-w-gpio-shutdown-not-working/4018/2

sudo systemctl status systemd-logind
○ systemd-logind.service
Loaded: masked (Reason: Unit systemd-logind.service is masked.)
Active: inactive (dead)

https://dietpi.com/forum/t/why-is-systemd-logind-service-masked-problems-with-kodi/4783/2

https://github.com/MichaIng/DietPi/discussions/6059

apt-get install libpam-systemd dbus

```
systemctl unmask systemd-logind.service
systemctl enable systemd-logind.service
systemctl start systemd-logind.service
```
