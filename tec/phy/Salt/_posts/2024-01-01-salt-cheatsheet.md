---
---

## Master

sudo salt '\*' saltutil.refresh_pillar
sudo journalctl -u salt-master.service --follow
sudo salt-run fileserver.file_list

sudo salt '\*' state.show_highstate saltenv=base

## Minions

sudo salt node01 grains.setval roles "['salt-master']"
salt node01 grains.append roles "salt-master"
sudo cat /etc/salt/grains
sudo salt node01 grains.delkey roles
sudo salt 'myRpaMinion' grains.append roles "uipath-robot"

sudo salt 'node42' system.set_computer_name node42
sudo salt "node42" system.get_pending_reboot
node42:
True

sudo salt 'node42' system.reboot 30 in_seconds=True only_on_pending_reboot=True message="Rebooting in 30 seconds"

## Windows Minions

### User Management

sudo salt -G 'os_family:Windows' user.current
sudo salt -G 'os_family:Windows' group.list_groups
sudo salt -G 'os_family:Windows' user.list_users
sudo salt 'myWindowsMinion' user.add Bob groups=Users
sudo salt 'myWindowsMinion' user.update Bob password_never_expires=Never #expiration_date does not work on Windows
sudo salt -G 'os_family:Windows' user.info Bob

sudo salt 'myWindowsMinion' user.chgroups Bob "Remote Desktop Users" append=True

### Updates

sudo salt -G 'os_family:Windows' win_wua.list install=True
sudo salt -G 'os_family:Windows' system.get_pending_reboot
sudo salt -G 'os_family:Windows' system.get_pending_update
sudo salt 'myWindowsMinion' system.reboot 30 in_seconds=True only_on_pending_reboot=True message="Rebooting in 30 seconds"

### Chocolatey

Install Chocolatey on all Windows minions:
sudo salt -G 'os_family:Windows' chocolatey.bootstrap
sudo salt -G 'os_family:Windows' cmd.run 'choco --version'

sudo salt 'myWindowsMinion' cmd.run "choco list"
sudo salt 'myWindowsMinion' cmd.run "choco source list"

#e.g. after a sudo salt 'myRpaMinion' grains.append roles "uipath-robot"
//// check quotes
sudo salt -G 'roles:uipath-robot' cmd.run "choco install uipathstudio --yes --source 'Z:\choco\packages' --install-arguments=\"'ADDLOCAL=DesktopFeature,Studio,Robot,ExcelAddin,ChromeExtension,EdgeExtension,RegisterService CUSTOM_NUGET_FEEDS=\"project-basturma-packages,https://www.myget.org/F/project-basturma-packages/api/v3/index.json\" ENABLE_PIP=1 TELEMETRY_ENABLED=0'\" --force --no-progress"
sudo salt -G 'roles:uipath-robot' cmd.run "choco uninstall uipathstudio"

sudo salt -G 'os_family:Windows' chocolatey.unbootstrap

### drive mapping

sudo salt 'myWindowsMinion' cmd.run 'net use'
sudo salt 'myWindowsMinion' cmd.run 'net use | find "Z:"'
sudo salt -G 'os_family:Windows' disk.usage

sudo salt 'myWindowsMinion' cmd.run " net use Z: /delete /y"
sudo salt 'node03' cmd.run "net use Z: \\\\edge\\share & dir Z: & choco install uipathstudio -y --source 'Z:\choco\pack>

sudo salt 'myWindowsMinion' state.apply windows.map_network_drive

### Housekeeping

sudo salt -G 'os_family:Windows' cmd.run "Get-ChildItem 'C:\Users\Public\Desktop' -Filter \*.
lnk | Remove-Item -Force" shell=powershell

## SDB

sudo salt-run sdb.get sdb://uipathcloud/cprimadotnet

sudo cat /etc/salt/master.d/sdb.conf
mysdb:
driver: yaml
files: - /srv/sdb/mysdb.yaml
uipathcloud:
driver: yaml
files: - /srv/sdb/uipathcloud.yaml

cat /srv/sdb/uipathcloud.yaml
cprimadotnet:

- name: cprimadotnet
- cloudUrl: https://cloud.uipath.com/
