---
---

OpenWRT URL: https://openwrt.org/toh/netgear/r7800

```bash
# ubus call system board
{
        "kernel": "5.15.150",
        "hostname": "myrouter",
        "system": "ARMv7 Processor rev 0 (v7l)",
        "model": "Netgear Nighthawk X4S R7800",
        "board_name": "netgear,r7800",
        "rootfs_type": "squashfs",
        "release": {
                "distribution": "OpenWrt",
                "version": "2x.y.z",
                "revision": "r12345-abc0123def",
                "target": "ipq806x/generic",
                "description": "OpenWrt 2x.y.z r12345-abc0123def"
        }
}
```

Excerpt from /etc/config/network

```
config switch
        option name 'switch0'
        option reset '1'
        option enable_vlan '1'

config switch_vlan
        option device 'switch0'
        option vlan '1'
        option ports '1 2 3 4 6t'

config switch_vlan
        option device 'switch0'
        option vlan '2'
        option ports '5 0t'
```
