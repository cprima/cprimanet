---
---

### Running Jenkins on Port 80 with `iptables` on GNU/Linux

Jenkins, the popular open-source automation server, usually runs on port 8080 by default. While this works for many setups, there might be times when you want to access Jenkins on the standard HTTP port, port 80. This article will walk you through how to achieve this using `iptables` on a GNU/Linux system, without having to modify Jenkins itself.

#### Prerequisites:

Before we begin, make sure you have the following in place:

1. **A GNU/Linux system**: This guide focuses on Debian-based distributions, but the principles apply to other distributions with slight modifications.
2. **Root or sudo access**: Adjusting port settings and manipulating `iptables` requires elevated privileges.
3. **Jenkins Installed**: If you don't have Jenkins installed yet, follow the [official Jenkins installation guide](https://www.jenkins.io/doc/book/installing/linux/).
4. **Familiarity with the terminal**: We'll be running commands and editing configuration files.
5. **A backup**: Always a good practice. Before making system changes, ensure you have backups of important data.

#### Step-by-step Guide:

##### 1. Confirm Jenkins is Running:

Before making changes, ensure that Jenkins is running properly on its default port. Access it in your browser:

```
http://YOUR_SERVER_IP:8080
```

If Jenkins is properly set up, you should see the Jenkins dashboard.

##### 2. Set up the `iptables` Rule:

`iptables` is a powerful tool for configuring IP packet filter rules in the Linux kernel. We'll use it to redirect traffic from port 80 to 8080:

```bash
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8080
```

This rule tells the system to take any traffic coming in on port 80 and reroute it to port 8080, where Jenkins is listening.

##### 3. Save the `iptables` Rule:

To ensure our rule persists across reboots, save the current `iptables` setup:

```bash
sudo sh -c "iptables-save > /etc/iptables.rules"
```

##### 4. Auto-apply the Rule on Boot:

To ensure the rule is applied every time your system starts, edit the `/etc/network/interfaces` file and append the following:

```bash
pre-up iptables-restore < /etc/iptables.rules
```

Alternatively, you can create an executable script in `/etc/network/if-pre-up.d/`:

```bash
#!/bin/sh
/sbin/iptables-restore < /etc/iptables.rules
```

Remember to make it executable:

```bash
sudo chmod +x /etc/network/if-pre-up.d/YOUR_SCRIPT_NAME
```

##### 5. Test the Setup:

After setting up the `iptables` rule and ensuring it will persist across reboots, restart your server or manually apply the rule:

```bash
sudo iptables-restore < /etc/iptables.rules
```

Now, when you access `http://YOUR_SERVER_IP` in a browser, it should load the Jenkins dashboard, effectively serving Jenkins on port 80.

#### Conclusion:

Using `iptables` to reroute traffic from port 80 to 8080 is an effective method to serve Jenkins on the standard HTTP port without changing its core configuration or running it with elevated privileges. This approach maintains the separation of concerns by letting Jenkins run as it always does while using native Linux tools to handle the port redirection. Always remember to monitor and back up your system configurations when making changes. Happy building!
