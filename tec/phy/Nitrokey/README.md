


The Nitrokey HSM is a lightweight hardware security module in a USB key form factor containing the SmartCard-HSM.

https://github.com/OpenSC/OpenSC/wiki/SmartCardHSM


A Hardware Security Module, HSM, is a device where secure key material is stored. This private data only be accessed by the HSM, it can never leave the device.

https://raymii.org/s/articles/Get_Started_With_The_Nitrokey_HSM.html#toc_2

Wrong SO pins are counted. When you have entered 15 wrong SO pins, the device is forever blocked and unusable. This is non-recoverable. The counter can not be reset as well.

https://raymii.org/s/articles/Get_Started_With_The_Nitrokey_HSM.html#toc_7


pkcs11-tool --module opensc-pkcs11.so --login --pin 1234567890 --keypairgen --key-type rsa:2048 --id 23 --label "HSM SSH key CPRIMA 2023"



C:\Program Files\OpenSC Project\OpenSC\tools> .\pkcs11-tool.exe --login --pin ****** --keypairgen --key-type rsa:2048 --id 23 --label "HSM SSH key CPRIMA 2023"


PS C:\Program Files\OpenSC Project\OpenSC\tools> .\pkcs15-tool.exe --read-ssh-key 23
Using reader with a card: Nitrokey Nitrokey HSM 0
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCCIkck+5YThaasD+LywvhXvePNlL7sHlsAnEwYCMz+1y24VwDenBKmdq7zGuLe7uNEcfAvA1dqRi6Ea+gEpr57wLXTc1m4HQIVr7OyMa8+YwoMSpLBvY4FDhg3LSbe6NzANTZdVf/9gjM9XDg0btl5US2fzLs0/RXrwZvLkEa9iiaRy+xCxKRrDOQWwl/jq+8APM1Mfdfu6y73uR2i9F5IW531wMNJVeQdBFYkqFymive0FvRUrC4IVQBBOyoB6VR1iQmSLImK/lZu7OZgPrMWz1kFfDxx7q0DX5/8epv6n1xCmSOvcipd1maaOwhD5vOtbn0UPSpe1o4T/7VQMm55 HSM SSH key CPRIMA 2023



Ubuntu
apt-get install pcscd pcsc-tools opensc


WSL must be version 2 to get USB devices

https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/


https://askubuntu.com/a/1406206







https://interworks.com/blog/2021/09/15/setting-up-ssh-agent-in-windows-for-passwordless-git-authentication/


ssh agent

Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service

PowerShell 7.3.1
PS C:\Users\cpm> ssh -T git@github.com
The authenticity of host 'github.com (140.82.121.4)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Enter PIN for 'SmartCard-HSM (UserPIN)':
Hi cprima! You've successfully authenticated, but GitHub does not provide shell access.
PS C:\Users\cpm>


https://github.com/buptczq/WinCryptSSHAgent



choco upgrade chocolatey



choco install wincrypt-sshagent
Chocolatey v1.2.1
Installing the following packages:
wincrypt-sshagent
By installing, you accept licenses for the packages.
Progress: Downloading wincrypt-sshagent 1.1.9... 100%

wincrypt-sshagent v1.1.9 [Approved]
wincrypt-sshagent package files install completed. Performing other installation steps.
The package wincrypt-sshagent wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):




OpenSSH Authentication Agent
disable
stop


WinCryptSSH -> system tray




PS C:\Program Files\OpenSC Project\OpenSC\tools> .\sc-hsm-tool.exe
Using reader with a card: Nitrokey Nitrokey HSM 0
Version              : 3.5
SmartCard-HSM has never been initialized. Please use --initialize to set SO-PIN and user PIN.


