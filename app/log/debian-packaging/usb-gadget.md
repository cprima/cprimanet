# Human Interface Devices HID with USB connection

Problem: To easily send the shortcut Ctrl Shift m

Solution: Use the Linux kernel on a Raspberry Pi Zero! (Or Zero W)

## Keyboards and the Linux kernel

For the Linux kernel a USB keyboard is one type of USB Human Interface Devices, implemented with its USB HID gadget driver.
The documentation at https://www.kernel.org/doc/Documentation/usb/gadget_hid.txt says:
> The HID Gadget driver provides emulation of USB Human Interface
> Devices (HID). The basic HID handling is done in the kernel,
> and HID reports can be sent/received through I/O on the
> /dev/hidgX character devices.

A HID report is the message that sent, in case of a keyboard the report will contain the keystrokes.

Quite astonishing that it is one driver that handles a myriad of USB Human Interface devices!

Besides the keyboard there might be other devices like mouse, joystick, keypad, device dock, gamepad and many more generic desktop usages. It is important that devices identify with their correct functionalities because applications will decide then how to interprete their input.

The Linux kernel HID Gaddget driver will not only get input from the device, but also provide the device data back, e.g. for a keyboard to light the small LED when Caps Lock is pressed.

For the full spec the website https://www.usb.org/ is the right place to look for the file "HID Usage Tables FOR Universal Serial Bus (USB)"

When plugged into a host, a device like a keyboard will register with a HID descriptor. Dies ist ein Array von Bytes und sieht bsw so aus: `59 05 01 09 06 a1 01 05 08 15 00 25 01 19 01 29 03 75 01 95 03 91 02 95 05 91 01 05 07 19 e0 29 e7 75 01 95 08 81 02 95 08 81 01 15 00 26 ff 00 19 00 2a ff 00 75 08 95 06 81 00 c0`

Here the output of a keyboard plugged into a computer running the Linux kernel:

```
 sudo hid-recorder
Available devices:
/dev/hidraw0:   Das Keyboard Das Keyboard P13
/dev/hidraw1:   Das Keyboard Das Keyboard P13
/dev/hidraw2:   Das Keyboard Das Keyboard P13
Select the device event number [0-2]: 0
# Das Keyboard Das Keyboard P13
# 0x05, 0x01,                    // Usage Page (Generic Desktop)        0
# 0x09, 0x06,                    // Usage (Keyboard)                    2
# 0xa1, 0x01,                    // Collection (Application)            4
# 0x05, 0x08,                    //  Usage Page (LEDs)                  6
# 0x15, 0x00,                    //  Logical Minimum (0)                8
# 0x25, 0x01,                    //  Logical Maximum (1)                10
# 0x19, 0x01,                    //  Usage Minimum (1)                  12
# 0x29, 0x03,                    //  Usage Maximum (3)                  14
# 0x75, 0x01,                    //  Report Size (1)                    16
# 0x95, 0x03,                    //  Report Count (3)                   18
# 0x91, 0x02,                    //  Output (Data,Var,Abs)              20
# 0x95, 0x05,                    //  Report Count (5)                   22
# 0x91, 0x01,                    //  Output (Cnst,Arr,Abs)              24
# 0x05, 0x07,                    //  Usage Page (Keyboard)              26
# 0x19, 0xe0,                    //  Usage Minimum (224)                28
# 0x29, 0xe7,                    //  Usage Maximum (231)                30
# 0x75, 0x01,                    //  Report Size (1)                    32
# 0x95, 0x08,                    //  Report Count (8)                   34
# 0x81, 0x02,                    //  Input (Data,Var,Abs)               36
# 0x95, 0x08,                    //  Report Count (8)                   38
# 0x81, 0x01,                    //  Input (Cnst,Arr,Abs)               40
# 0x15, 0x00,                    //  Logical Minimum (0)                42
# 0x26, 0xff, 0x00,              //  Logical Maximum (255)              44
# 0x19, 0x00,                    //  Usage Minimum (0)                  47
# 0x2a, 0xff, 0x00,              //  Usage Maximum (255)                49
# 0x75, 0x08,                    //  Report Size (8)                    52
# 0x95, 0x06,                    //  Report Count (6)                   54
# 0x81, 0x00,                    //  Input (Data,Arr,Abs)               56
# 0xc0,                          // End Collection                      58
#
R: 59 05 01 09 06 a1 01 05 08 15 00 25 01 19 01 29 03 75 01 95 03 91 02 95 05 91 01 05 07 19 e0 29 e7 75 01 95 08 81 02 95 08 81 01 15 00 26 ff 00 19 00 2a ff 00 75 08 95 06 81 00 c0
N: Das Keyboard Das Keyboard P13
I: 3 24f0 0105
```

Dies beinhaltet Informationen über jeden Button/jedes Scrollrad/jede Mausachse, deren Minimal- und Maximalwerte, mit wieviel Bytes die Werte abgebildet werden und ob es absolute oder relative Werte sind.

Additionally to that, a device registers with serialnumber, version, vendor identifier, manufacturer name, USB protocol version, language, and more.


## How to pretend to be a keyboard

With the above long preface one piece of information is missing: The Raspberry Pi Zero is
xxxxxxxxxxxxxx

To register a keyboard device with the kernel all it takes is to *write into* the configfs underneath /sys/kernel/config/usb_gadget/, to be precise into subdirectories that the kernel driver expects:
(Sidenote: At compile time this is configured with CONFIGFS_FS)

Finally the gadget must be enabled.

How to do this is documented at https://www.kernel.org/doc/html/latest/usb/gadget_configfs.html
It is pretty straightforward. Quoting the documentation:

> An example directory structure might look like this:
>
>```.
>./strings
>```
>./strings/0x409
>./strings/0x409/serialnumber
>./strings/0x409/product
>./strings/0x409/manufacturer
>./configs
>./configs/c.1
>./configs/c.1/ncm.usb0 -> ../../../../usb_gadget/g1/functions/ncm.usb0
>./configs/c.1/strings
>./configs/c.1/strings/0x409
>./configs/c.1/strings/0x409/configuration
>./configs/c.1/bmAttributes
>./configs/c.1/MaxPower
>./functions
>./functions/ncm.usb0
>./functions/ncm.usb0/ifname
>./functions/ncm.usb0/qmult
>./functions/ncm.usb0/host_addr
>./functions/ncm.usb0/dev_addr
>./UDC
>./bcdUSB
>./bcdDevice
>./idProduct
>./idVendor
>./bMaxPacketSize0
>./bDeviceProtocol
>./bDeviceSubClass
>./bDeviceClass
>```

To write into these file all it takes is an echo command, like ´echo echo "Christian Prior-Mamulyan" > strings/0x409/manufacturer`

As this keyboard will not be plugged in or otherwise raise an event to trigger its configuration, a suitable point in time might be right after booting, because systemd makes this quite easy to do.
And because it is about kernel configuration this needs to be done as root.

## OK, let's go

A few decisions need to be made upfront:

serialnumber
manufacturer
product

/usr/bin/RPiZeroHID.sh

```bash
#!/usr/bin/env bash
#/** 
#  * This script ... ConfigFS kernel USB gadget system startup configuration
#  * 
#  * Copyright (c) 2019 Christian Prior
#  * Licensed under the MIT License. See LICENSE file in the project root for full license information.
#  * 
#  * Usage: ...
#  * 
#  * @TODO: ...
#  * 
#  */

set -o nounset #exit on undeclared variable
__BASEDIR="/sys/kernel/config/usb_gadget/"
__SERIALNUMBER=1
__MANUFACTURER="me"
__PRODUCT="mySoftwareKeyboard"

if [ ! -d "$__BASEDIR" ]; then
  echo "Are you really on a Raspberry Pi Zero? Because /sys/kernel/config/usb_gadget/ does not exist! Exiting."
  exit 1
fi

read -p "Enter serialnumber: " __SERIALNUMBER
read -p "Enter manufacturer: " __MANUFACTURER
read -p "Enter productname: " __PRODUCT

cd $__BASEDIR


```



```
[Unit]
Description=ConfigFS kernel USB gadget system startup configuration

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/RPiZeroHID.sh
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
~                              
```

## Finally sending keystrokes

// modifier: Shift 30 Ctrl Shift 48



## Links

https://en.wikipedia.org/wiki/Human_interface_device
https://gitlab.freedesktop.org/libevdev/hid-tools
https://who-t.blogspot.com/2018/12/understanding-hid-report-descriptors.html
https://embeddedguruji.blogspot.com/2019/04/learning-usb-hid-in-linux-part-7.html
https://www.kernel.org/doc/html/latest/usb/gadget_configfs.html
