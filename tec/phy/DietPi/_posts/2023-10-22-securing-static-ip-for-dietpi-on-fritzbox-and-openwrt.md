---
layout: post
title: "Securing a Static IP for Your DietPi Raspberry Pi: A Guide for Fritz!Box and OpenWRT Users"
#date: YYYY-MM-DD HH:MM:SS +/-TTTT
#author: Author
#component:
#categories: [Category]
#tags: [Tag]
abstract: "Whether you're on Fritz!Box or leveraging the power of OpenWRT, ensuring your Raspberry Pi with DietPi always has the same IP can be a game-changer for consistent network setups and services. Dive into this guide as we walk you through setting a fixed IP lease, simplifying your network management and boosting reliability."
---

Setting a fixed IP lease, often known as a static DHCP lease or DHCP reservation, ensures that a device always receives the same IP address when it requests an IP from the router. Here's how you can set it up for a Raspberry Pi running DietPi, both on a Fritz!Box and on a router running OpenWRT:

### Fritz!Box:

1. **Access the Fritz!Box user interface**:

   - Open a web browser and go to `http://fritz.box` or the IP address of your Fritz!Box.

2. **Login**:

   - Enter your password to log in to the Fritz!Box user interface.

3. **Navigate to Home Network**:

   - From the main menu, select `Home Network` and then `Network`.

4. **View Network Connections**:

   - Click on the `Network Connections` or `Devices` tab (depending on your Fritz!Box version).

5. **Find the Raspberry Pi**:

   - Look for the Raspberry Pi (it might show up as DietPi or the hostname you've set) in the list of devices.

6. **Edit Device Settings**:

   - Click on the device name or the `Edit` button (which might look like a pencil or gear icon).

7. **Assign a Fixed IP Address**:

   - In the device settings, you'll find an option that says "Always assign this network device the same IPv4 address" or similar wording. Enable this option.
   - The system will usually auto-fill the current IP address of the Raspberry Pi. If not, or if you wish to change it, input the desired static IP here.

8. **Save Changes**:
   - Click on `OK` or `Apply` to save the settings.

### OpenWRT:

1. **Access the OpenWRT LuCI interface**:

   - Open a web browser and navigate to `http://192.168.1.1` or the IP address you've set for your OpenWRT router.

2. **Login**:

   - Enter your password to access the OpenWRT LuCI interface.

3. **Navigate to Network Settings**:

   - On the top menu, select `Network`, then choose `DHCP and DNS`.

4. **Static Leases Section**:

   - Scroll down to find the `Static Leases` section.

5. **Add a New Static Lease**:

   - Click on `Add` or `Add entry`. A new row will appear with fields to fill out.

6. **Fill in the Details**:

   - `MAC Address`: Enter the MAC address of your Raspberry Pi.
   - `IPv4 Address`: Enter the desired static IP address you want to assign to the Raspberry Pi.
   - `Hostname`: This can be left as is or set to the hostname of the Raspberry Pi.

7. **Save & Apply**:
   - Click `Save`, and then click `Save & Apply`.

For both methods, once the configuration is done, it's a good practice to reboot both the Raspberry Pi and the router to ensure the settings take effect. Ensure that the static IP address you're assigning doesn't conflict with other devices or the DHCP pool range.
