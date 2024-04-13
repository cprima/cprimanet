---
layout: post
title: "How to Cross-Compile Caddy in WSL2 for OpenWRT on MIPS"
date: 2023-11-26
component: TA_PTC_058
---

I have a GL.iNet GL-AR750S travel router, and want to use that device as a gateway into a homelab. I want to run Caddy on the router to serve as a reverse proxy for my homelab services. The GL-AR750S runs OpenWRT, but the Caddy package on https://caddyserver.com/download for Linux mips does not generate successfully. So I need to cross-compile Caddy for the router's MIPS architecture. Easy to do with xcaddy and Go.

## References

- the OpenWRT device page https://openwrt.org/toh/gl.inet/gl-ar750s
- Caddy build instructions https://caddyserver.com/docs/build
- Initscripts on OpenWRT: https://openwrt.org/docs/techref/initscripts

## Prerequisites

Before we begin, make sure you have the following prerequisites in place:

1. A Windows machine with WSL2 installed and configured.
2. Knowledge of your travel router's MIPS architecture details.
3. Go installed on WSL2 and confirmed working (e.g., `go version`).

## Step 1: Set Up WSL2

If you haven't already set up WSL2 on your Windows machine, you can follow Microsoft's official documentation to do so.

## Step 2: Install Go

Use the Linux AMD64 tarball to install Go on WSL2. You can find the latest version of the tarball on the Go downloads page.

```
wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
rm -rf /usr/local/go && sudo tar -C /usr/local -xzf /tmp/go1.21.4.linux-amd64.tar.gz

```

Add to .bashrc:

```bash
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```

## Step 3: Clone Caddy Repository

In your WSL2 terminal, navigate to your development directory and clone the Caddy repository:

Git Clone Command: [link](https://github.com/caddyserver/caddy.git)
Change Directory Command: `cd caddy`

## Step 4: Cross-Compile Caddy

Next, you need to configure Caddy for cross-compilation. Use the following command, replacing `<ARCH>` with your router's MIPS architecture (e.g., `mipsle`):

```bash
 GOOS=linux GOARCH=mips GOMIPS=softfloat xcaddy build latest --with github.com/caddy-dns/cloudflare
```

This command sets the GOOS and GOARCH environment variables to target your router's architecture and builds Caddy accordingly.

## Step 6: Transfer Caddy to Your Router

Transfer the compiled Caddy binary to your router running OpenWRT. You can use SCP, FTP, or any other method you prefer to copy the binary to your router.

```
scp caddy  root@192.168.8.1:
```

### Step 7: Install and Configure Caddy

On your router, install and configure Caddy as you normally would on an OpenWRT device:

Create and make executable the init script /etc/init.d/caddy:

```bash
#!/bin/sh /etc/rc.common
# Custom Caddy init script for OpenWrt
# Copyright (C) 2023 Christian Prior-Mamulyan <cprior@gmail.com>

START=99
STOP=10
EXTRA_COMMANDS="adapt"
EXTRA_HELP="        adapt  Running Caddy adapt command"
PROG=/usr/bin/caddy
CADDY_FILE=/etc/caddy/Caddyfile
export CADDY_ACME_INWX_PASSWORD="Wzmk,dwina.iJ6,37"

start() {
        echo "Starting Caddy with $CADDY_FILE"
        "$PROG" start --config "$CADDY_FILE" --pidfile /var/run/caddy.pid --adapter caddyfile
}

stop() {
        echo "Stopping Caddy"
        "$PROG" stop
}


reload() {
        echo "Reloading Caddy configuration"
        "$PROG" validate --config "$CADDY_FILE"
        "$PROG" fmt "$CADDY_FILE" --overwrite
        "$PROG" reload --config "$CADDY_FILE"
}


adapt() {
        echo "Running Caddy adapt command"
        "$PROG" validate --config "$CADDY_FILE"
        "$PROG" fmt "$CADDY_FILE" --overwrite
        "$PROG" adapt --config "$CADDY_FILE" --pretty
}

```

And here a sample Caddyfile to get started:

```
:2015 {
    header Content-Type text/html
    respond "<html><head><title>Hello World!</title></head><body>Hello World!</body></html>"
}

:2016 {
    reverse_proxy localhost:80
}
```

On a default GL.iNet GL-AR750S this make these two URLs accessible via a browser:

- [http://192.168.8.1:2015](http://192.168.8.1:2015)

- [http://192.168.8.1:2016](http://192.168.8.1:2016)
