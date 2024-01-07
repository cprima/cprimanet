# sudosudo  salt '*' saltutil.sync_grains

import os

def hardware_info():
    grains = {}
    
    if os.path.exists("/proc/cpuinfo"):
        with open("/proc/cpuinfo", "r") as f:
            for line in f.readlines():
                if "Model" in line:
                    _, model = line.strip().split(": ")
                    grains["hardware_model"] = model.replace(" ", "").strip()
                    break

    return grains
