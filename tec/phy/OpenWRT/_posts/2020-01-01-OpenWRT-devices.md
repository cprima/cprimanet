---
---

In OpenWRT, devices are referenced in different configuration files depending on their type and purpose. Here’s a general overview of how devices are managed and referenced in OpenWRT:

### Types of Devices

1. **Network Devices**: These include physical network interfaces (e.g., `eth0`, `eth1`) and virtual interfaces (e.g., VLAN interfaces like `eth0.1`).
2. **Wireless Devices**: These are radio interfaces used for wireless networking (e.g., `radio0`, `radio1`).

### Configuration Files

1. **/etc/config/network**: This file contains the configuration for wired network interfaces, VLANs, and bridges.

2. **/etc/config/wireless**: This file contains the configuration for wireless interfaces. Wireless devices (radios) are typically defined here.

3. **/etc/config/system**: This file includes system-wide settings and some device-specific settings.

### Where Devices Are Defined

1. **Network Devices**:

   - Physical and virtual network interfaces are defined in `/etc/config/network`.
   - Bridges and VLANs are also defined in `/etc/config/network`.

2. **Wireless Devices**:
   - Wireless radios (e.g., `radio0`, `radio1`) are defined in `/etc/config/wireless`.
   - Each radio device has its settings, such as the wireless mode, SSID, encryption, and more.

### UCI Commands to List Devices

- **List Network Devices**:

  ```sh
  uci show network
  ```

- **List Wireless Devices**:
  ```sh
  uci show wireless
  ```

### Example Explanation

1. **/etc/config/network** might contain:

   ```plaintext
   config interface 'lan'
       option proto 'static'
       option ipaddr '192.168.1.1'
       option netmask '255.255.255.0'
       option device 'br-lan'

   config device 'br-lan'
       option type 'bridge'
       list ports 'eth0 eth1'
   ```

2. **/etc/config/wireless** might contain:

   ```plaintext
   config wifi-device 'radio0'
       option type 'mac80211'
       option channel '11'
       option hwmode '11g'
       option path 'pci0000:00/0000:00:1c.0/0000:02:00.0'
       option htmode 'HT20'
       option country 'US'

   config wifi-iface
       option device 'radio0'
       option network 'lan'
       option mode 'ap'
       option ssid 'OpenWRT'
       option encryption 'psk2'
       option key 'yourpassword'
   ```

### Devices in OpenWRT

- **Network Devices**: Referenced in `/etc/config/network`, defined for wired interfaces and virtual interfaces.
- **Wireless Devices**: Referenced in `/etc/config/wireless`, defined specifically for wireless radios.

### Listing All Devices

To see all network-related devices managed by UCI, you can use:

```sh
uci show network
```

For wireless devices:

```sh
uci show wireless
```

These commands list all configurations and help you see how devices are referenced and configured.

### Additional Notes

- **Physical Interfaces**: Directly correspond to hardware interfaces on your router.
- **Logical Interfaces**: Created through configurations like bridges or VLANs and can combine multiple physical interfaces.

This should help clarify how devices are managed and referenced in OpenWRT and where to look for their configurations.
