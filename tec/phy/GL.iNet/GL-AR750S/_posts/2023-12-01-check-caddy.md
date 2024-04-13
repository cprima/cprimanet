---
layout: post
title: "How to check with cron if caddy is running on OpenWRT"
date: 2023-12-01
component: TA_PTC_058
---

For this to work caddy must have been started in /etc/init.d/caddy with the --pidfile option.

```sh
#!/bin/sh

PID_FILE="/var/run/caddy.pid"

# Check if the PID file exists
if [ ! -f "$PID_FILE" ]; then
    echo "PID file does not exist. Starting Caddy..."
    /etc/init.d/caddy start
else
    # Extract PID from the file
    PID=$(cat "$PID_FILE")

    # Check if the process is running
    if ! kill -0 "$PID" > /dev/null 2>&1; then
        echo "Caddy is not running. Starting Caddy..."
        /etc/init.d/caddy start
    else
        echo "Caddy is running."
    fi
fi
```
