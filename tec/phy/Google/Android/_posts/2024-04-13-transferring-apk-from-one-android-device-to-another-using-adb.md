---
layout: post
title: "Transferring an APK from One Android Device to Another Using ADB"
date: 2024-04-13
excerpt: This tutorial details the steps required to transfer an APK file from one Android device to another using ADB, highlighting the necessity of root access on the source device and the procedural use of a computer as an intermediary.
---

## Transferring an APK from One Android Device to Another Using ADB

Transferring an application package (APK) from one Android device to another involves several steps and requires the use of a computer as an intermediary to facilitate the transfer using Android Debug Bridge (ADB). This method is particularly useful for developers and tech enthusiasts who wish to install software manually. It assumes the source Android device is rooted, which is essential for accessing the APK files located in secure parts of the device's storage.

![/tec/phy/Google/Android/resources/images/transferring-apk-from-one-android-device-to-another-using-adb.png](/tec/phy/Google/Android/resources/images/transferring-apk-from-one-android-device-to-another-using-adb.png)

### Equipment and Setup Required

1. **Rooted Source Android Device**: This device must be rooted. Root access allows the extraction of APK files from secure storage locations that are not accessible on unrooted devices.
2. **Target Android Device**: This device will receive the APK file. It does not need to be rooted unless the APK requires root access to function properly.

3. **Computer**: Acts as the conduit for the APK file between the two Android devices. It must have ADB installed—a component of the Android SDK Platform-Tools.

4. **USB Cables**: These are used to connect both the source and target Android devices to the computer.

### Procedure

#### Step 1: Prepare the Devices

- **Enable USB Debugging on Both Devices**: Navigate to `Settings > System > Developer options` on both Android devices and enable USB debugging. This setting is crucial for allowing ADB commands to interface with the devices.

#### Step 2: Connect the Source Device to the Computer

- **Connect the source device to the computer using a USB cable**. Confirm the connection type on the device is set to "File Transfer" mode if prompted.

#### Step 3: Extract the APK Using ADB

- **Open a command prompt or terminal window on the computer**. Verify the device is connected by executing `adb devices`. The device should appear in the list.
- **Use ADB to pull the APK file from the source device**. The command will look like this:
  ```
  adb pull /path/to/apk.apk /local/path
  ```
  The exact path where the APK is stored can vary, but typically, it would be within `/data/app/`.

#### Step 4: Install the APK on the Target Device

When installing APKs on an Android device via ADB, there are two main methods depending on the structure of the application package: single APK file installation and combined APKs installation, often referred to as split APKs. The single APK method involves a straightforward installation of one complete package, while the combined APKs method is used for apps that have been split into multiple APKs for modular architecture, reducing unnecessary resource use by allowing the installation of only the components needed for a particular device configuration.

Here are the two variants for installing APKs:

- **Connect the target device to the computer** using another USB cable. Use the `adb devices` command again to ensure it is listed.

1. **Single File Installation**:

   ```bash
   adb install /local/path/apk.apk
   ```

   This command installs a single APK file, which contains all the application's necessary resources and code.

2. **Combined APKs Installation**:
   ```bash
   adb install-multiple /local/path/base.apk /local/path/split_config.arm64_v8a.apk /local/path/split_config.en.apk /local/path/split_config.xxhdpi.apk
   ```
   This command installs multiple APK files associated with a single application, such as base APKs and configuration-specific APKs for different device architectures, languages, and screen densities.

## How to find the APK path on the source device

```
PS C:\Users\cpm>  adb shell
klte:/ $ su -
klte:/ # ls /data/app/
~~0RAYsW12He-KyjwRTm6VLA==  ~~BVOAzQC_c2siRkpMeJ7SAQ==  ~~UCKNo9mwtfkOGkO2SlyTOA==  ~~h6eGk2hw7qY1pR9Q9j0mog==  ~~t88iukoKQEQegCXpwskpsQ==
~~1IJNa2rQTA3mkPD40RLLdg==  ~~Eo0D4Qmmj6PMddcthqgFBA==  ~~W04RUPx0kRPvdehshWAbRg==  ~~i3q565htfy2hSfYLpu4ZqQ==  ~~tZLmkgMJs-24apFpL8RYsg==
~~1oRGPrK36WMoswhzB5jsxw==  ~~GfAIX_4PaF8dfFbOnnMg2Q==  ~~Y2WMCc3PS-DF2wW6UMQVnQ==  ~~if4XFmE5iKeg7heOoNsRwQ==  ~~vdBYpV6UZ50h2nNA3uPplA==
~~40HbVXEh-MnCfZ86yYkGFg==  ~~IGWKyu-41EsSgF3l3gAKBw==  ~~Yd8xFICtfYjD12C29bW8FA==  ~~l1IU70R-3HHfb2BqI-11sA==  ~~vfmuyXMVXacVbsUTUqy4wA==
~~8NDzakBpN8ZBi7fMjWzFHw==  ~~MF5j00aWlyCQY5ktFPYdsA==  ~~_DhgvqdijNgZVLk-zCO6yQ==  ~~ntYOVKF69gKe02oT4abGKQ==  ~~vvGnZHk4TYcAXH9tG-C0jA==
~~8XVNFmNnxXNK7zGk38PWMQ==  ~~REtUBw-rg4V0AhSZfVNt9g==  ~~_EpEz-gMsLuGiaNqbx-mcg==  ~~o7gRotX7uji2uwLy-y9jxA==  ~~wpupAB49jRxrVWnQ70anAw==
~~9zvx-BtPq3JZnEYohqflQw==  ~~S2hLl7LGjWxjeWFE9FaGWQ==  ~~dHyYYaYYatWy86XrqH1Ysg==  ~~p1oFZtrw2nA3Q8zDR2_eaQ==  ~~xOZer0ZituNRxDR9zc38iA==
~~A-AX-rNUq0DIpvV1AC-iSw==  ~~S9xH-Bi5lknSE_dM7AydkQ==  ~~dwYHSgXLYOYr4_zurALIhA==  ~~ppkHaPfPCN4RbED_X-XPmQ==
~~BD01JYcWqvg7mT-d67ZG1Q==  ~~TGvC49DriB8zIP2gl8T3gg==  ~~fv_en5OEeYlnrhWC-550Ng==  ~~rR6B03CedjfSvZAWGI6IHA==
~~BSCX6hEtdttLXjYj8js32w==  ~~TQyjTvgtp6BDTSD4TkjYqg==  ~~gu5IxCUddWYcdvIx28RsuQ==  ~~sJBVHYXlzd6Yb_fpGrCI0w==
klte:/ #
```

Using the `ls` command with the options -ls, you can list the contents of the `/data/app/` directory. This directory contains the APK files of the installed applications on the device. The APK files are stored in subdirectories with names that appear as a series of characters and numbers. To identify the APK file you want to extract, you can look at the timestamp of the folder in comparison to the date the app was installed, the package name of the application or the name of the APK file itself.

### Conclusion

This method provides a straightforward way to transfer APK files between Android devices using ADB. The requirement for the source device to be rooted is key, as it allows access to the full filesystem, enabling the extraction of APKs directly from the device storage. This technique is valuable for degooglefied devices, custom ROM users, and developers who need to manually install applications on their devices. By following these steps, you can seamlessly transfer APK files from one Android device to another without relying on the Google Play Store or other third-party services.
