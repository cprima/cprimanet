hen you perform a sysupgrade on an OpenWrt device, the additional packages you have installed are not preserved by default. Here’s what happens and what you can do to manage your installed packages:

What Happens After a Sysupgrade:
Firmware Overwrite: The sysupgrade process installs the new firmware image, which typically overwrites the existing system. This means any additional packages installed will be removed unless they are included in the new firmware image.

Configuration Files: If you choose to preserve settings during the sysupgrade (-c option in the command line or checking the "Keep settings" box in LuCI), most of your configuration files in /etc/config and some other specific directories will be retained. However, the binaries and data files of the additional packages will be lost.

cat /etc/config/custom-installed-packages.txt
ddns-scripts
ddns-scripts-services
luci-app-ddns
bind-host
wget-ssl

cat /etc/config/custom-installed-packages | xargs -r opkg install
Package ca-bundle (20230311-1) installed in root is up to date.
Package ddns-scripts (2.8.2-42) installed in root is up to date.
Package ddns-scripts-services (2.8.2-42) installed in root is up to date.
Package luci-app-ddns (git-23.346.52990-28c4a65) installed in root is up to date.
Installing bind-host (9.18.24-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/packages/bind-host_9.18.24-1_arm_cortex-a15_neon-vfpv4.ipk
Installing libatomic1 (12.3.0-4) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/targets/ipq806x/generic/packages/libatomic1_12.3.0-4_arm_cortex-a15_neon-vfpv4.ipk
Installing libopenssl3 (3.0.13-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/base/libopenssl3_3.0.13-1_arm_cortex-a15_neon-vfpv4.ipk
Installing zlib (1.2.13-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/base/zlib_1.2.13-1_arm_cortex-a15_neon-vfpv4.ipk
Installing librt (1.2.4-4) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/targets/ipq806x/generic/packages/librt_1.2.4-4_arm_cortex-a15_neon-vfpv4.ipk
Installing libuv1 (1.48.0-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/packages/libuv1_1.48.0-1_arm_cortex-a15_neon-vfpv4.ipk
Installing libnghttp2-14 (1.57.0-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/packages/libnghttp2-14_1.57.0-1_arm_cortex-a15_neon-vfpv4.ipk
Installing bind-libs (9.18.24-1) to root...
Downloading https://downloads.openwrt.org/releases/23.05.0/packages/arm_cortex-a15_neon-vfpv4/packages/bind-libs_9.18.24-1_arm_cortex-a15_neon-vfpv4.ipk
Package uclient-fetch (2023-04-13-007d9454-1) installed in root is up to date.
Configuring libatomic1.
Configuring libopenssl3.
Configuring zlib.
Configuring librt.
Configuring libuv1.
Configuring libnghttp2-14.
Configuring bind-libs.
Configuring bind-host.
