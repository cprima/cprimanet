

## Hardware

Raspberry Pi baremetal
32GB drive

## OS

DietPi
sudo apt-get install vim curl wget screen git

## Jenkins
sudo apt install openjdk-11-jre

curl https://pkg.jenkins.io/debian/jenkins.io.key | gpg --dearmor | sudo tee /usr/share/keyrings/jenkins-archive-keyring.gpg >/dev/null

vim /etc/apt/sources.list.d/jenkins.list
deb [signed-by=/usr/share/keyrings/jenkins-archive-keyring.gpg] https://pkg.jenkins.io/debian binary/
sudo apt update
sudo apt install jenkins

```

Created symlink /etc/systemd/system/multi-user.target.wants/jenkins.service → /lib/systemd/system/jenkins.service.
Job for jenkins.service failed because a timeout was exceeded.
See "systemctl status jenkins.service" and "journalctl -xe" for details.
invoke-rc.d: initscript jenkins, action "start" failed.
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/lib/systemd/system/jenkins.service; enabled; vendor preset: enabled)
     Active: activating (auto-restart) (Result: timeout) since Sat 2023-01-14 06:00:39 CET; 24ms ago
    Process: 7831 ExecStart=/usr/bin/jenkins (code=exited, status=143)
   Main PID: 7831 (code=exited, status=143)
     Status: "Jenkins stopped"
        CPU: 4min 30.056s
dpkg: error processing package jenkins (--configure):
 installed jenkins package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 jenkins
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

restart jenkins - just a timeout

sudo cat /var/lib/jenkins/secrets/initialAdminPassword
495496d1951d4f38ac29601276a0ba4b

