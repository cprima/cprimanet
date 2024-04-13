---
layout: post
title: "How to Recreate a Windows Recovery Partition From Scratch"
date: 2023-12-10
categories: Windows Recovery Environment
---

## Introduction

This post provides a step-by-step guide on how to recreate a Windows Recovery Environment (Windows RE) from scratch. This process involves deleting an existing recovery partition, creating a new one, and configuring Windows RE to use the new partition. This can be particularly useful if you need to resize your main Windows partition or if your existing recovery environment has become corrupt.

## Deleting the Existing Recovery Partition

To start, you need to delete the existing recovery partition. Open a Command Prompt with administrative privileges and start diskpart:

```
diskpart
```

List the disks available and select the disk where your Windows installation is located:

```
list disk
select disk 0
```

List the partitions, identify the recovery partition, and delete it:

```
list partition
select partition X
delete partition override
```

Replace `X` with the number of your recovery partition.

## Creating a New Recovery Partition

Create a new 1GB partition for Windows RE:

```
create partition primary size=1024
format fs=ntfs quick
assign letter=R
```

Set the correct ID and attributes for the new partition:

```
set id=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC
gpt attributes=0x8000000000000001
```

Exit diskpart:

```
exit
```

## Aside: Understanding GPT Attributes and Set ID

### GPT Attributes

The GUID Partition Table (GPT) is a standard for the layout of partition tables on a physical storage device, such as a hard disk or solid-state drive. GPT is part of the Unified Extensible Firmware Interface (UEFI) standard, which has become increasingly common in modern computers, replacing the older BIOS system.

When you modify the GPT attributes of a partition, you're essentially setting certain flags that tell the system how to treat that partition. For example:

```
gpt attributes=0x8000000000000001
```

This command sets specific attributes for the selected partition:

- The `0x8000000000000001` is a hexadecimal number where each bit represents a different attribute.
- The bit `0x8000000000000000` (the highest bit) is commonly used to indicate that a partition is a system partition.
- The lowest bit `0x1` marks the partition as required for the system to boot.

### Set ID

The `set id` command in DiskPart is used to change the partition type of a selected partition. Each partition type has a unique identifier, known as a GUID, that tells the operating system how to interact with it.

In the context of creating a Windows Recovery Environment, the command:

```
set id=DE94BBA4-06D1-4D40-A16A-BFD50179D6AC
```

is used to set the partition's type to a specific GUID that identifies it as a Windows Recovery partition. This GUID is recognized by Windows and helps the operating system understand the purpose and function of this partition.

By setting the correct GPT attributes and partition ID, you ensure that the recovery partition is correctly identified and used by Windows for recovery purposes.

## Mounting the Windows Image

Mount your Windows installation media and identify the correct index of the Windows version. Use DISM to mount the image:

```
Dism.exe /Mount-Wim /WimFile:E:\sources\install.wim /index:6 /mountdir:C:\Users\cpm\Downloads\mountpoint /readonly
```

Replace `E:\` with your installation media drive letter and adjust the mount directory path as needed.

## Enabling Windows RE

Re-open Command Prompt as administrator and configure Windows RE to use the new partition:

```
reagentc /setreimage /path R:\Recovery\WindowsRE /target C:\Windows
reagentc /enable
reagentc /info
```

Confirm the configuration with the reagentc /info command.

## Conclusion

You have now successfully recreated the Windows Recovery Environment on your system. This setup ensures that you have a dedicated recovery partition, which can be invaluable for system recovery and maintenance tasks.

Remember to back up your data before undertaking tasks like this, as they can potentially lead to data loss if not done correctly.
