---
checklists: []
---


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

Admin Powershell:
usbipd wsl list
BUSID  VID:PID    DEVICE                                                        STATE
1-7    20a0:4230  Microsoft Usbccid Smartcard Reader (WUDF)                     Not attached
1-8    8087:0aaa  Intel(R) Wireless Bluetooth(R)                                Not attached
4-1    046d:c52b  Logitech USB Input Device, USB Input Device                   Not attached

usbipd wsl attach --busid 1-7


sudo pcscd #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------------------------


cat .ssh/config
Host wambra
    User tlwin
    HostName wambra
    PKCS11Provider opensc-pkcs11.so

Host github.com
    User git
    HostName github.com
    PKCS11Provider opensc-pkcs11.so

Host companion
    User companion
    HostName 10.38.20.13
    PKCS11Provider opensc-pkcs11.so



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



sc-hsm-tool.exe 



Firmware Update
Firmware updates for the SmartCard-HSM are available in the PKI-as-a-Service Portal.

The firmware can only be updated on an empty SmartCard-HSM. You need to remove all keys, certificates and data files first.

During the firmware update, the SmartCard-HSM receives a new device authentication certificate, so any previous registration at the PKI-as-a-Service portal will need to be renewed.

https://www.smartcard-hsm.com/firmware.html



# 2024-10

https://github.com/johndoe31415/hsmwiz

https://www.youtube.com/watch?v=qbKkrArkXkY


PowerShell Admin
usbipd list
Connected:
BUSID  VID:PID    DEVICE                                                        STATE
1-7    20a0:4230  Microsoft Usbccid Smartcard Reader (WUDF)                     Not shared
1-8    8087:0aaa  Intel(R) Wireless Bluetooth(R)                                Not shared
3-1    046d:c52b  Logitech USB Input Device, USB Input Device                   Not shared

usbipd bind --busid 1-7

PowerShell User (or Admin)

 usbipd attach --wsl --busid 1-7


WSL
sudo pcscd
sc-hsm-tool
Using reader with a card: Nitrokey Nitrokey HSM (DENK02009140000         ) 00 00
Version              : 3.6
Config options       :
  User PIN reset with SO-PIN enabled
SO-PIN tries left    : 15
User PIN tries left  : 3
DKEK shares          : 1
DKEK key check value : E94F16B464D58B35



## mechanisms

pkcs11-tool --list-mechanisms
Using slot 0 with a present token (0x0)
Supported mechanisms:
  SHA-1, digest
  SHA224, digest
  SHA256, digest
  SHA384, digest
  SHA512, digest
  MD5, digest
  RIPEMD160, digest
  GOSTR3411, digest
  ECDSA, keySize={192,521}, hw, sign, other flags=0x1d00000
  ECDSA-SHA1, keySize={192,521}, hw, sign, other flags=0x1d00000
  ECDH1-COFACTOR-DERIVE, keySize={192,521}, hw, derive, other flags=0x1d00000
  ECDH1-DERIVE, keySize={192,521}, hw, derive, other flags=0x1d00000
  ECDSA-KEY-PAIR-GEN, keySize={192,521}, hw, generate_key_pair, other flags=0x1d00000
  RSA-X-509, keySize={1024,4096}, hw, decrypt, sign, verify
  RSA-PKCS, keySize={1024,4096}, hw, decrypt, sign, verify
  SHA1-RSA-PKCS, keySize={1024,4096}, sign, verify
  SHA224-RSA-PKCS, keySize={1024,4096}, sign, verify
  SHA256-RSA-PKCS, keySize={1024,4096}, sign, verify
  SHA384-RSA-PKCS, keySize={1024,4096}, sign, verify
  SHA512-RSA-PKCS, keySize={1024,4096}, sign, verify
  MD5-RSA-PKCS, keySize={1024,4096}, sign, verify
  RIPEMD160-RSA-PKCS, keySize={1024,4096}, sign, verify
  RSA-PKCS-PSS, keySize={1024,4096}, hw, sign, verify
  SHA1-RSA-PKCS-PSS, keySize={1024,4096}, sign, verify
  SHA224-RSA-PKCS-PSS, keySize={1024,4096}, sign, verify
  SHA256-RSA-PKCS-PSS, keySize={1024,4096}, sign, verify
  SHA384-RSA-PKCS-PSS, keySize={1024,4096}, sign, verify
  SHA512-RSA-PKCS-PSS, keySize={1024,4096}, sign, verify
  RSA-PKCS-KEY-PAIR-GEN, keySize={1024,4096}, generate_key_pair


pkcs11-tool --login --keypairgen --key-type rsa:4096 --label "SSH CA"
pkcs15-tool --read-ssh-key 7ce88a769c6a39d7d796eb3280a4b39953aa5151
# scp to ssh server
pkcs11-tool --login --keypairgen --key-type EC:secp256r1 --label "SSH HSM cpm 2024-10"
pkcs11-tool --list-objects
pkcs15-tool --read-ssh-key d29f8be82376c1bc8f561dccbe1e0df245c9e213
vim .ssh/id-SSH-HSM-cpm-2024-10.pub


list all keys on HSM

  ssh-keygen -D /usr/lib/x86_64-linux-gnu/pkcs11/opensc-pkcs11.so -e
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDAVTz/9UKAjNu+nAqxO06S70p+QOD97/Lhp/wgaEBaFR2ycBJoGBKSb87ZhiMnuZA+zVvmdf9v8LIWM+vEUls+YuHIy54F04vXrr2/RQfn942R/pfvJDxC973q7YVeLpMc95N/5fedzfxh8RJBNAL0E6NzErTgQYHrwsM1ScVD5QYMV7kJFSRfl+Zls4u3uUWKWpVoFvL0+g/kxqM+2z4QLsWmuNNZ6VCX8mmzO+sJMZK+gL5eWAN5z0ThrY3WVHrBKncj5XsRulNw6DZ+kyMyzsUDw2Ii31wkLgrSSkyWzczNq2ozA2vS/jxTrEpzcsmaiCIOCy74YUqXEjPtDbpicSiWsCmNFzA0UKi9kDyEISNJcD9i5cA/iLCL/kBzgIvAM/AirGuwX2U21aAL/5639dQQkumMKF5c60A8ADqD5HdSCzUhV+eALROwtUXo/H8OwX4ZzS8pWW3/H5hmDXzq3lb1gBloY0oQQqOnQMT2wUAcuBNarmbQqV0C0/XCzzrH2Kyw3vTRnzY4vKLlp/ei1I2wG75A/FQ27A56OPsqfQ0kQLArCsEVPTNxwboO7SYRTb8mH6gqz4qh7HH05ZCcdg3R3FYnlYurWLFwHWivPAeWyayEVamcIb+YFraSRf/hlS3Y9yox0yHPfecHEFnexoWD0WOJDX1FXo3DlIRDJQ== SSH CA
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJrdY2PEJpsQ72kxF22X9PLeJ5OleMsJJ9AgB5cN8e8zwLD487Ldk5uAvaQw+/qyb6gYTI18cwpu31inANMkCzs= SSH HSM cpm 2024-10

ssh-keygen -D /usr/lib/x86_64-linux-gnu/pkcs11/opensc-pkcs11.so -s ~/.ssh/id-SSH-CA.pub -I "SSH HSM cpm thru 2024-11-30" -V "-1d:20241130" ~/.ssh/id-SSH-HSM-cpm-2024-10.pub


## backup restore

pkcs15-tool --dump
Using reader with a card: Nitrokey Nitrokey HSM (DENK02009140000         ) 00 00
PKCS#15 Card [net.cprima.hsm02]:
        Version        : 0
        Serial number  : DENK0200914
        Manufacturer ID: www.CardContact.de
        Flags          :

PIN [UserPIN]
        Object Flags   : [0x03], private, modifiable
        Auth ID        : 02
        ID             : 01
        Flags          : [0x812], local, initialized, exchangeRefData
        Length         : min_len:6, max_len:15, stored_len:0
        Pad char       : 0x00
        Reference      : 129 (0x81)
        Type           : ascii-numeric
        Path           : e82b0601040181c31f0201::
        Tries left     : 3

PIN [SOPIN]
        Object Flags   : [0x01], private
        ID             : 02
        Flags          : [0x9A], local, unblock-disabled, initialized, soPin
        Length         : min_len:16, max_len:16, stored_len:0
        Pad char       : 0x00
        Reference      : 136 (0x88)
        Type           : bcd
        Path           : e82b0601040181c31f0201::
        Tries left     : 15

Private RSA Key [SSH CA]
        Object Flags   : [0x03], private, modifiable
        Usage          : [0x2E], decrypt, sign, signRecover, unwrap
        Access Flags   : [0x1D], sensitive, alwaysSensitive, neverExtract, local
        ModLength      : 4096
        Key ref        : 1 (0x01)
        Native         : yes
        Auth ID        : 01
        ID             : 7ce88a769c6a39d7d796eb3280a4b39953aa5151
        MD:guid        : 44dc72b1-c69b-f695-7950-93c7f35b79ab

Private EC Key [SSH HSM cpm 2024-10]
        Object Flags   : [0x03], private, modifiable
        Usage          : [0x10C], sign, signRecover, derive
        Access Flags   : [0x1D], sensitive, alwaysSensitive, neverExtract, local
        FieldLength    : 256
        Key ref        : 2 (0x02)
        Native         : yes
        Auth ID        : 01
        ID             : d29f8be82376c1bc8f561dccbe1e0df245c9e213
        MD:guid        : ec5c9944-c887-6acd-439a-472a518ad785

Public RSA Key [SSH CA]
        Object Flags   : [0x00]
        Usage          : [0x51], encrypt, wrap, verify
        Access Flags   : [0x02], extract
        ModLength      : 4096
        Key ref        : 0 (0x00)
        Native         : no
        ID             : 7ce88a769c6a39d7d796eb3280a4b39953aa5151
        DirectValue    : <present>

Public EC Key [SSH HSM cpm 2024-10]
        Object Flags   : [0x00]
        Usage          : [0x40], verify
        Access Flags   : [0x02], extract
        FieldLength    : 256
        Key ref        : 0 (0x00)
        Native         : no
        ID             : d29f8be82376c1bc8f561dccbe1e0df245c9e213
        DirectValue    : <present>

sc-hsm-tool --wrap-key wrapped-key-SSH-CA-1.bin --key-reference 1
sc-hsm-tool --wrap-key wrapped-key-SSH-HSM-cpm-2024-10-1.bin --key-reference 2




