---
layout: post
title: "pcbuild 2023"
component: 
date:   2023-01-06 00:00:00 +0100
abstract: ""
---


* TOC
{:toc}


#{{ include.headingmodifier }} foo

![foo](/biz/production/pcbuild/images/pcbuild-4k-capture-pc-2023.svg){:class="resize"}

{% include_relative includes/pcpartpicker-4k-capture-pc-2023.md headingmodifier="#" %}


Tier A - required to be based on ZVS primary topology (LLC or phase shift resonant), have ripple below 50mV under all load situations up-to 110% overload, <=3% transient response on 12V rail, <=3% 12v voltage deviation from nominal. Fan with =>30k hours MTBF at 40°C (generally non-plain-sleeve bearing) or be fanless. All capacitors rated for 105°C. Minimum 18AWG gauge wires for hot 12V leads on GPU/EPS/ATX cables, on pig-tail cables - at least to the first connector, 20AWG to the second or for ground leads.

https://docs.google.com/spreadsheets/d/1eL0893Ramlwk6E3s3uSvH1_juom7SMG5SCNzP2Uov8w/edit#gid=1214219159

https://cultists.network/140/psu-tier-list/



#{{ include.headingmodifier }} First Boot

BIOS Update

With MSI: As easy as placing a file in the root of a USB stick, place it in specific USB port and press a special button (all on the rear side).




#{{ include.headingmodifier }} Install OS

https://www.microsoft.com/en-us/software-download/windows10

https://support.microsoft.com/en-us/windows/create-installation-media-for-windows-99a58364-8c02-206f-aa6f-40c3b507420d

Create Windows install media

Get Window key

slmgr.vbs /dlv
