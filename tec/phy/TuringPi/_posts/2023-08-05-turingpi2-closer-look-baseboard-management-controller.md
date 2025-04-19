---
layout: post
title: Baseboard Management Controller (BMC)
component: TA_PTC_051
date:   2023-08-05 12:00:00 +0100
abstract: "The TuringPi 2 has made notable strides in the realm of multi-node computing platforms. Among its standout features is the integrated Baseboard Management Controller (BMC), which provides an array of management and monitoring functionalities."
---

## The Turing Pi 2: A Closer Look at its Baseboard Management Controller (BMC)

In recent years, the demand for robust and compact computing solutions has been on the rise. One such board making waves in the tech community is the Turing Pi 2. Today, we'll delve into one of its most standout features - the Baseboard Management Controller (BMC).

### What is a Baseboard Management Controller (BMC)?

Before we proceed to discuss the BMC on the Turing Pi 2, it's essential to understand what a BMC is. A BMC is a specialized microcontroller embedded in a computer or server motherboard. Its primary role is to oversee the system's hardware components, even when the main system is off or non-functional.

A BMC can monitor several parameters like temperatures, fan speeds, and power supply voltages. Moreover, it provides remote management capabilities, such as rebooting a system, updating firmware, or logging performance metrics for analysis.

### BMC on the Turing Pi 2

The Turing Pi 2 is equipped with an Allwinner T113-S3, responsible for its BMC functionality. Essentially, think of this as a mini-computer built directly into the board's main structure. 

#### Specifications:
- **Controller:** Allwinner T113-S3
- **Processor:** ARM Cortex-A7 Dual-Core
- **Memory:** 128MB DDR3
- **Storage:** 1GB NAND Flash Memory (MX35LF1GE4AB)
- **Additional Storage:** SD Card slot 

#### Firmware:

The Turing Pi 2’s BMC firmware is an open-source project. It's worth noting that while many BMCs in the market have proprietary firmware, Turing Pi 2 opts for a transparent approach. The open-source nature means that users can access and modify the source code to cater to their specific requirements.

#### Operating System:

The BMC on the Turing Pi 2 runs on a Linux OS based on Buildroot. This version offers fundamental tools resembling other Linux distributions. However, it's streamlined and does not possess a package system. Consequently, if you need to add new software, it usually necessitates recompiling and re-flashing.

Moreover, the board's internal eMMC memory is not designed for long-term storage of scripts or ISO images. It's recommended to utilize the SD card interface for these purposes.

#### BMC’s SD Card Slot:

An SD card slot is available, linked directly to the BMC. During startup, the BMC attempts to access the SD card, which can be used to store data such as ISO images or scripts. The system is compatible with various file systems like exFAT, NTFS, FAT32, and EXT4.

### Why BMC is Essential:

For administrators and tech enthusiasts, BMC offers a few compelling advantages:

1. **Remote Management:** Particularly beneficial when physical access to a machine is restricted.
4. **Power Control:** Through the BMC, users have the capability to manage the power state of their TuringPi 2. This includes operations like powering on, off, or even resetting the system remotely.
3. **Efficiency:** Allows for firmware updates without full system reboots, reducing downtime.

remove: 2. **Diagnostics:** The BMC can store logs and metrics, aiding in troubleshooting hardware issues.


In conclusion, the Baseboard Management Controller (BMC) on the Turing Pi 2 is an embodiment of the board's dedication to flexibility, management, and performance optimization. Its open-source nature and integration into a compact computing solution like the Turing Pi 2 make it a noteworthy feature for tech professionals and enthusiasts.