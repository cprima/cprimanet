---
layout: post
title: "Salt in the Homelab: Targeting Raspberry Pi"
component: TA_PTC_056
date: 2023-10-18 12:00:00 +0100
abstract: "Utilizing SaltStack's advanced functionalities, like custom grains and nodegroups, offers refined targeting abilities for specific devices like the Raspberry Pi. By crafting tailored grains and employing nodegroups, system administrators can seamlessly manage and automate configurations across Raspberry Pi units, ensuring uniformity and efficiency in large-scale deployments."
---

## **Leveraging SaltStack: Custom Grains, Nodegroups, and State Files**

### **Introduction**

SaltStack is a powerful automation and configuration management tool. In a recent deep dive, several advanced features of SaltStack were explored, including custom grains, nodegroups, and state file best practices.

### **1. Custom Grains**

Custom grains are extensions to Salt's built-in system information gathering capabilities. They allow users to fetch or compute additional details about a system.

#### **Common Use-Cases for Custom Grains**:

- **Cloud Metadata**: Extract cloud-specific details, like instance ID or region.
- **Application Versions**: Detect versions of applications installed on minions.
- **Roles Assignment**: Designate roles like `webserver` or `database` to minions.
- **Environment Data**: Label nodes based on environment types (`prod`, `dev`, etc.).
- **Network Topology**: Gather specific network configurations or details.
- **Security Posture**: Determine if certain security measures are in place.

#### **Creating Custom Grains**:

Custom grains are typically written in Python. For instance, a grain was written to extract the "Model" line from `/proc/cpuinfo` commonly found on Raspberry Pi devices:

```python
import os

def hardware_info():
    grains = {}

    if os.path.exists("/proc/cpuinfo"):
        with open("/proc/cpuinfo", "r") as f:
            for line in f.readlines():
                if "Model" in line:
                    _, model = line.strip().split(": ")
                    grains["hardware_model"] = model.strip().replace(" ", "")
                    break
    return grains
```

### **2. Nodegroups**

Nodegroups simplify the targeting of a group of minions based on specific criteria. Instead of using complex matchers each time, you can define nodegroups in the Salt master configuration:

```yaml
nodegroups:
  raspberrypi_group: "G@hardware_model:RaspberryPi4ModelBRev1.4 or G@hardware_model:RaspberryPi4ModelBRev1.5"
```

These groups can then be easily targeted:

```bash
sudo salt -N raspberrypi_group test.ping
```

### **3. Minion roles**

Minions can be assigned roles using a config file. For instance, a minion can be assigned the role `webserver` in `/etc/salt/minion.d/grains.conf`:

```yaml
grains:
  roles:
    - webserver
```

In a top.sls file, minions can be targeted based on their roles:

```yaml
base:
  "G@roles:webserver":
    - match: grain
    - apache
```

Or on the command line:

```bash
sudo salt -G 'roles:webserver' test.ping
```

### **Conclusion**

SaltStack offers versatile features that can cater to specific needs, whether it's gathering custom system information with grains, logically grouping minions using nodegroups, or defining system states with state files. Proper utilization of these features can streamline system management and automation tasks.
