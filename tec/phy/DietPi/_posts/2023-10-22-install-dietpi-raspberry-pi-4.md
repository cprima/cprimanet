---
abstract: "DietPi is a lightweight Debian-based distribution optimized for single board computers, including the Raspberry Pi. Here's a step-by-step guide on how to install DietPi on a Raspberry Pi 4"
---

DietPi is a lightweight Debian-based distribution optimized for single board computers, including the Raspberry Pi. Here's a step-by-step guide on how to install DietPi on a Raspberry Pi 4:

### Prerequisites:

1. **Hardware**:

   - Raspberry Pi 4
   - MicroSD Card (8GB or more recommended)
   - MicroSD Card Reader
   - Power supply for Raspberry Pi 4
   - Optional: Keyboard, Mouse, and Monitor for direct interaction (otherwise you can SSH into it)

2. **Software**:
   - A tool to flash the MicroSD card (e.g., [Balena Etcher](https://www.balena.io/etcher/))
   - DietPi image for Raspberry Pi 4 (You can download it from the [DietPi Download Page](https://dietpi.com/#download))

### Installation Steps:

1. **Download the DietPi Image**:

   - Visit the [DietPi Download Page](https://dietpi.com/#download).
   - Under the Raspberry Pi section, click on "Download" for the Raspberry Pi 4 model.
   - Save the `.img` file to your computer.

2. **Flash the DietPi Image to the MicroSD Card**:

   - Insert your MicroSD card into the card reader and connect it to your computer.
   - Open Balena Etcher (or another flashing tool of your choice).
   - Click on "Flash from file" and select the DietPi `.img` file you downloaded.
   - Click on "Select target" and choose your MicroSD card from the list.
   - Click "Flash!" and wait for the process to complete.

3. **Initial Boot**:

   - Once the flashing process is complete, safely eject the MicroSD card from your computer.
   - Insert the MicroSD card into the Raspberry Pi 4.
   - Connect peripherals like a keyboard, mouse, and monitor if you're planning to use them.
   - Power on the Raspberry Pi 4.

4. **First Boot Configuration**:

   - Upon first boot, DietPi will start an automatic setup process which includes resizing the filesystem, updating the OS, and a few other housekeeping tasks.
   - After the initial setup, you'll be presented with the DietPi software selection menu. From here, you can choose additional software to install or just proceed with the default selections.

5. **System Setup**:

   - You'll be prompted to set a root password. Make sure to choose a strong password.
   - Configure your timezone, language, and other locale settings as prompted.
   - Configure networking as needed. If you're using an Ethernet connection, it should work out of the box. For Wi-Fi, you'll need to provide your SSID and passphrase.

6. **Software Installation**:

   - If you selected any additional software during the software selection phase, DietPi will now install those packages. This may take some time depending on what you've chosen.

7. **Finalize Setup**:

   - Once everything is configured, DietPi will reboot, and you should be greeted with a login prompt. You can log in using the root user and the password you set earlier.

8. **SSH Access** (Optional but recommended):
   - If you didn't connect a monitor and peripherals, you can SSH into your Raspberry Pi. The default hostname is `dietpi`, so from another device on the same network, you can use:
     ```
     ssh root@dietpi.local
     ```
   - Use the root password you set earlier to log in.

You should now have DietPi up and running on your Raspberry Pi 4! From here, you can further customize your installation, add more software, and configure the system as needed.
