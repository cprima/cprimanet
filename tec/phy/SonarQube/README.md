




https://sourceforge.net/projects/wrapper/

https://sourceforge.net/projects/wrapper/files/wrapper/Wrapper_3.5.51_20221111/wrapper-linux-armhf-32-3.5.51.tar.gz/download


brings elastic in ./elasticsearch - not really good

useradd -m sonarqube
passwd sonarqube
#q3
usermod -s /bin/bash sonarqube
#gpasswd -a sonarqube sudo


sudo apt install postgresql

sudo su postgres
createuser sonarqube -P --interactive


postgres@brubu:/root$ createuser sonarqube -P --interactive
Enter password for new role:
Enter it again:
Shall the new role be a superuser? (y/n) y
postgres@brubu:/root$


sudo apt-get install openssh-client

unzip sonarqube-9.8.0.63668.zip
mv sonarqube-9.8.0.63668 /opt/sonarqube
tar xvzf wrapper-linux-armhf-32-3.5.51.tar.gz
mv wrapper-linux-armhf-32-3.5.51 /opt/wrapper
cd /opt/
cp -r sonarqube/bin/linux-x86-64/ sonarqube/bin/linux-pi/
cp -r wrapper/bin/wrapper sonarqube/bin/linux-pi
cp -f wrapper/lib/libwrapper.so sonarqube/bin/linux-pi/lib/libwrapper.so
cp -f wrapper/lib/wrapper.jar sonarqube/bin/linux-pi/lib/wrapper.jar
chown -R sonarqube:sonarqube /opt/sonarqube/

initial login admin:admin


https://computingforgeeks.com/install-sonarqube-code-review-centos/


sonar-scanner
https://docs.sonarqube.org/latest/analyzing-source-code/scanners/sonarscanner/


https://stackoverflow.com/a/51448773

/etc/sysctl.conf
vm.max_map_count=262144

sysctl --system
sysctl vm.max_map_count

sudo vim /etc/systemd/system/sonarqube.service
[Unit]
Description=SonarQube service
After=syslog.target network.target

[Service]
Type=forking
ExecStart=/opt/sonarqube/bin/linux-pi/sonar.sh start
ExecStop=/opt/sonarqube/bin/linux-pi/sonar.sh stop
LimitNOFILE=65536
LimitNPROC=4096
User=sonar
Group=sonar
Restart=on-failure

[Install]
WantedBy=multi-user.target