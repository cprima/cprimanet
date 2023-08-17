---
layout: post
title: Redefining (Homelab) Cluster Computing
component: TA_PTC_051
date:   2023-08-01 12:00:00 +0100
abstract: "Cluster computing has grown in popularity and necessity, offering increased processing power, better load balancing, and enhanced redundancy. A significant player in this space is the TuringPi 2, a cluster board designed for edge computing and learning environments."
---



## TuringPi 2: Redefining (Homelab) Cluster Computing

Cluster computing has grown in popularity and necessity, offering increased processing power, better load balancing, and enhanced redundancy. A significant player in this space is the TuringPi 2, a cluster board designed for edge computing and learning environments.

### What is the TuringPi 2?

The Turing Pi 2 is a compact cluster board that supports multiple compute modules for scalable computing, enhanced by an integrated BMC for advanced management. This innovative solution addresses the common challenges faced in building clusters by streamlining networking, power management, storage, and administration.

### Nodes Supported by TuringPi 2:

The TuringPi 2 stands out due to its ability to support a variety of nodes. Specifically:

1. **Turing RK1 Modules**: This is the Turing Pi's default compute module.
2. **Raspberry Pi Compute Module 4 (CM4)**: The Raspberry Pi CM4 is a compact board from the Raspberry Pi series, offering better performance, memory, and I/O options than its predecessor, yet in a smaller form factor. It's designed for embedded computing and provides the reliability and flexibility required for various applications.
3. **NVIDIA Jetson Modules**: NVIDIA Jetson modules are popular for their AI capabilities. They are compact computing solutions tailored for AI projects, robotics, and embedded computing.

### Cluster Essentials on the TuringPi 2:

#### 1. Networking:

The TuringPi 2 ensures seamless networking with its integrated 1 Gbps Ethernet network and an onboard managed switch. These features enable high-speed connections between nodes, eliminating the need for messy wires or external devices.

#### 2. Power:

Integrated power management is at the core of TuringPi 2's design. The board draws power from an ATX 24 Pin socket, ensuring consistent energy supply to all modules.

##### Great combination: Pico PSU

The Pico PSU is a compact, direct plug-in power supply unit (PSU) designed primarily for small form factor PCs, especially those housed in mini-ITX cases. This PSU connects directly to the motherboard, bypassing the need for the traditional bulky power supply units found in standard desktops. Although compact, the Pico PSU requires an external power adapter, typically rated at 12V and varying amperes depending on the model and power needs. Due to its minimalistic design and size, the Pico PSU is favored in systems where space is at a premium, such as embedded systems, compact desktops, and various DIY projects.

The Pico PSU is a product of Mini-Box, a division of Ituner Networks Corp. They are credited with pioneering the design of these compact and efficient power supply units tailored for small form factor PCs and various other applications. Mini-Box has been a significant player in the mini-ITX and embedded market, offering a range of products beyond just the Pico PSU.

https://www.google.com/search?q=Pico+PSU

https://docs.turingpi.com/docs/turing-pi2-powering-on-the-device

<!--//
Pico PSU:
-> https://www.myelectronics.nl/us/19-inch-2u-mini-itx-case-for-dual-mini-itx-short-d.html
> On the back of the case is an 8mm hole for the pico PSU DC input cable, which is compatible with most DC PSUs
//-->

#### 3. Storage:

The TuringPi 2 offers extendable storage solutions, allowing users to easily integrate additional storage to the cluster. Each node slot provides a straightforward mechanism to incorporate storage modules, ensuring the smooth running of data-intensive tasks.

>
> on Node 3, right? SATA ports are connected to this node.
>
> Which OS are you running there? If this is Ubuntu, please run `sudo apt install linux-modules-extra-raspi` and restart the module
>
> Source: [https://docs.turingpi.com/discuss/64dbda70d6faa500748b4b29](https://docs.turingpi.com/discuss/64dbda70d6faa500748b4b29)


#### 4. Administration:

An essential part of any cluster is efficient administration. The TuringPi 2 shines here with its built-in Baseboard Management Controller (BMC). This tool facilitates easy node management, monitoring of system health, automation of installation tasks, and much more. Essentially, it ensures that you can manage, automate, and troubleshoot the cluster to a certain extend.


##### What is the meaning of all the different blinking led's on the turing pi?

> The LEDs:
> 
> - a green LED next to the ATX power connection - turns on when the power supply is attached and powered
> - another green LED next to the ATX power connector - turns on when at least one node is powered
> - red LEDs next to the nodes (from the back panel side) - turn on when you power the node on
> - orange blinking LED near the red power LED of Node 1 - network activity of the BMC
> - green LEDs next to the nodes (from the ATX power connector side) - module network is up
> - orange LEDs next to the nodes (from the ATX power connector side) - module network activity
> - green LED on the top of the CM4 adapter board - power indicator
> - green LED on the bottom of the CM4 adapter board - blinks with the compute module activity
>
> Source: [https://docs.turingpi.com/discuss/64d5680a965bd500789a41c4](https://docs.turingpi.com/discuss/64d5680a965bd500789a41c4)

