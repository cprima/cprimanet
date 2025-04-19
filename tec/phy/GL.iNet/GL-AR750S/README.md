---
component: TA_PTC_058
---

Cross compile caddy for the GL-AR750S

```bash
GOOS=linux GOARCH=mips GOMIPS=softfloat xcaddy build latest
```

OpenWRT toh:

https://openwrt.org/toh/gl.inet/gl-ar750s

More settings > Advanced > LUCI not working? Clear Browser Cookies (even needed after just a LAN IP change).
