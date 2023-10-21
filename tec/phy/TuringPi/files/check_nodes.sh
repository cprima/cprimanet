#!/bin/bash

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Check if /root/.ssh/id_rsa.pub exists
if [[ ! -f "/root/.ssh/id_rsa.pub" ]]; then
    echo "/root/.ssh/id_rsa.pub does not exist. Exiting."
    exit 1
fi

# Check if not running on TuringPi with armv7l architecture
if [ "$(uname -m)" != "armv7l" ] || [ "$(uname -n)" != "turingpi" ]; then
    echo "Error: This script can only run on TuringPi with armv7l architecture."
    exit 1
fi

# Initialize an array to keep track of resolved IPs
declare -A resolved_ips

# Create a copy of hostnames to loop through
hosts_to_resolve=("$@")

# Loop until all hostnames have their IPs resolved
while [[ ${#hosts_to_resolve[@]} -gt 0 ]]; do
    clear
    # Loop over the unresolved hostnames
    for i in "${!hosts_to_resolve[@]}"; do
        hostname="${hosts_to_resolve[$i]}"

        # Get the IP of the hostname
        ip=$(getent hosts "$hostname" | awk '{print $1}')

        # If IP is resolved, test it with ping
        if [[ -n "$ip" ]]; then
            # Check if the IP is responsive using ping
            if ping -c 1 "$ip" &>/dev/null; then
                resolved_ips["$hostname"]=1

                # ssh-keygen -f "/home/dietpi/.ssh/known_hosts" -R "$hostname"
                # sudo ssh-keygen -f "/home/dietpi/.ssh/known_hosts" -R "$ip"
                # ssh-keygen -f "/home/dietpi/.ssh/known_hosts" -R "$hostname"
                # sudo ssh-keygen -f "/home/dietpi/.ssh/known_hosts" -R "$ip"

                # # Copy the ssh key to the remote host
                # # sudo ssh-copy-id -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i /root/.ssh/id_rsa.pub root@"$hostname"

                # # Execute the specified commands on the remote host
                # sshpass -p 'dietpi' ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no -o StrictHostKeyChecking=no -v root@"$hostname" "
                #     if [[ -f /etc/apt/sources.list.d/salt.list ]]; then
                #         rm /etc/apt/sources.list.d/salt.list || { echo 'Failed to remove salt.list'; exit 1; }
                #     fi
                #     curl -fsSL -o /etc/apt/keyrings/salt-archive-keyring.gpg https://repo.saltproject.io/py3/debian/11/armhf/latest/salt-archive-keyring.gpg || { echo 'Failed to download salt-archive-keyring.gpg'; exit 1; }
                #     echo 'deb [signed-by=/etc/apt/keyrings/salt-archive-keyring.gpg arch=armhf] https://repo.saltproject.io/py3/debian/11/armhf/latest bullseye main' | tee /etc/apt/sources.list.d/salt.list || { echo 'Failed to update salt.list'; exit 1; }
                #     apt-get update || { echo 'apt-get update failed'; exit 1; }
                #     apt-get install -y salt-minion || { echo 'Failed to install salt-minion'; exit 1; }
                #     echo 'master: brubu' | tee /etc/salt/minion.d/10_master.conf || { echo 'Failed to configure salt-minion'; exit 1; }
                #     systemctl start salt-minion || { echo 'Failed to start salt-minion'; exit 1; }
                # "

                # # Check if the ssh command was successful
                # if [[ $? -eq 0 ]]; then
                #     # Remove the resolved hostname from the list
                #     unset 'hosts_to_resolve[i]'
                # else
                #     echo "SSH command to $hostname failed."
                # fi
                unset 'hosts_to_resolve[i]'
            else
                echo "Ping to IP $ip for hostname $hostname was unsuccessful. Breaking..."
                #break 2  # This will break out of the for loop and the enclosing while loop
                break
            fi
        else
            echo "Failed to resolve IP for hostname: $hostname"
        fi
        sleep 2
    done
    echo "Sleeping..."
    sleep 8 # Sleep for 10 seconds before retrying
    echo "Retrying..."
    sleep 1 # Sleep for 10 seconds before retrying
done

echo "All operations have been performed on each host."
