

# CompanionPi


Companionpi is a repo and a subproject of companion to

- build companion images with Packr
- provide a curl'able installer file

CompanionPi by default installs Companion v3 and tries to do it's best for existing v2 installations (based on presence of /usr/local/src/companion).

The CompanionPi bash scripts are using NodeJS for bash dialog prompts, e.g. node "/usr/local/src/companionpi/update-prompt/main.js"


# Companion

tech stack
- fnm (works with .node-version)
- nodejs
- yarn
- some apt packages

## Versions

- stable https://api.bitfocus.io/v1/product/companion/packages?branch=stable&limit=999
- beta https://api.bitfocus.io/v1/product/companion/packages?branch=beta&limit=999
- experimental https://api.bitfocus.io/v1/product/companion/packages?branch=experimental&limit=999

## Version differences

### v2

- config file location: /home/companion/companion/db
- run command: /usr/local/src/companion && /opt/fnm/aliases/default/bin/node headless_ip.js 0.0.0.0
- installation: git checkout to /usr/local/src/companion

### v3

- config file location: /home/companion/.config/companion-nodejs/v3.0/db
- run command: /opt/companion/node-runtime/bin/node /opt/companion/main.js --extra-module-path /opt/companion-module-dev
- installation: untar into /opt/companion



# CompanionPi

The file install.sh calls update.sh (install.sh was introduced at about the same time as v3, @see: https://github.com/bitfocus/companion-pi/blob/dd11d9c466d1fab8ff0a50f12af72fa1e4b8cfdf/update.sh for last "pure" v2 version )


install.sh

- check if supported architecture x64, amd64, arm64
- Must be run as root
- companion version to install (based on github branch)
- adduser companion
- apt depedencis git zip unzip curl libusb-1.0-0-dev libudev-dev
- install fnm to /opt/fnm
  - set a default version
- git clone https://github.com/bitfocus/companion-pi.git
- execute ./update.sh
- install update script dependencies with yarn
- systemctl enable companion
- echo "export PATH=/opt/fnm/aliases/default/bin:\$PATH" >> /home/companion/.bashrc
- print message

missing in install.sh

- usage

update.sh

- ensure fnm is in path
- mkdir /opt/companion-module-dev
- companion v2 and v3 decision
- v2
  - in /usr/local/src/companion git fetch aa
  - select version
  - switch to branch
  - fnm use; fnm default; npm install yarn
  - increase swapfile
  - yarn config timeout
  - export node options
  - yarn update
  - swapoff
- v3
  - fnm use; fnm default; npm install yarn
  - select version
  - wget tarball
  - delete /opt/companion
  - copy from tarball into /opt/companion
- copy udev rules
- if sudo sudoers config
- adduser -q companion gpio
- adduser -q companion dialout
- fix bug in 3.0.0-rc2 by mkdir /home/companion/.config/companion-nodejs
- install systemd service file with ExecStart=/usr/local/src/companionpi/launch.sh
  - v2 /opt/fnm/aliases/default/bin/node headless_ip.js 0.0.0.0
  - v3 /opt/companion/node-runtime/bin/node /opt/companion/main.js --extra-module-path /opt/companion-module-dev
- install scripts companion-* to /usr/local/bin/
- install motd



# Run

/home/companion/.bashrc
export PATH=/opt/fnm/aliases/default/bin:$PATH

