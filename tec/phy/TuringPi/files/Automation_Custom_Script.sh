#!/bin/bash

#Automation_Custom_Script.sh

if [[ -f /etc/apt/sources.list.d/salt.list ]]; then
    rm /etc/apt/sources.list.d/salt.list || {
        echo 'Failed to remove salt.list'
    }
fi
curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring.gpg https://repo.saltproject.io/py3/debian/11/armhf/latest/salt-archive-keyring.gpg || {
    echo 'Failed to download salt-archive-keyring.gpg'
}
echo 'deb [signed-by=/etc/apt/keyrings/salt-archive-keyring.gpg arch=armhf] https://repo.saltproject.io/py3/debian/11/armhf/latest bullseye main' | tee /etc/apt/sources.list.d/salt.list || {
    echo 'Failed to update salt.list'
}
apt-get update || {
    echo 'apt-get update failed'
}
apt-get install -y salt-minion || {
    echo 'Failed to install salt-minion'
}
echo 'master: salt' | tee /etc/salt/minion.d/10_master.conf || {
    echo 'Failed to configure salt-minion'
}
systemctl restart salt-minion || {
    echo 'Failed to restart salt-minion'
}
