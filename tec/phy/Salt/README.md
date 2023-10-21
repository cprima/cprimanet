---
component: TA_PTC_056
---

-L Also install salt-cloud and required python-libcloud package
-M Also install salt-master
-A Pass the salt-master DNS name or IP. This will be stored under
${BS_SALT_ETC_DIR}/minion.d/99-master-address.conf
-i Pass the salt-minion id. This will be stored under
${BS_SALT_ETC_DIR}/minion_id

### master

`./bootstrap-salt.sh -M -A brubu -i brubu -L`

### minion

https://github.com/saltstack/salt-bootstrap

sudo curl -L https://bootstrap.saltproject.io | sudo sh -s -- -P -A salt-master stable

## rpi

sudo apt-get install -y curl gnupg
curl -L https://repo.saltproject.io/py3/debian/11/arm64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
echo "deb http://repo.saltproject.io/py3/debian/11/arm64/latest bullseye main" | sudo tee /etc/apt/sources.list.d/saltstack.list
sudo apt-get update
sudo apt-get install -y salt-minion
sudo vim /etc/salt/minion.d/99-master-address.conf
master: salt-master
sudo systemctl start salt-minion
sudo systemctl enable salt-minion

## on master:

sudo salt -G 'cpuarch:aarch64' test.ping
brubu:
True
sarmum:
True

cat /etc/salt/master.d/nodegroups.conf
nodegroups:
raspberrypis: 'G@osarch:arm64 and G@cpuarch:aarch64'

sudo salt -N raspberrypis test.ping
