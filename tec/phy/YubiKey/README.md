---

---


https://developers.yubico.com/PIV/Guides/SSH_with_PIV_and_PKCS11.html

https://peters-christoph.de/blog/server/yubikey-piv-ssh-client-mit-windows-10/


```
yubico-piv-tool.exe  -s 9a -a generate --pin-policy=never --touch-policy=always -o cpm.yubikey-2023-02.ssh.2023.cprima.net.pem
yubico-piv-tool.exe -a verify-pin -a selfsign-certificate --valid-days=340 -s 9a -S "/CN=cpm.yubikey-2023-02/OU=SSH 2023/O=cprima.net/" -i cpm.yubikey-2023-02.ssh.2023.cprima.net.pem -o cpm.yubikey-2023-02.ssh.2023.cprima.net.crt
yubico-piv-tool -a import-certificate -s 9a -i cpm.yubikey-2023-02.ssh.2023.cprima.net.crt

```
when self-signing touch the YubiKey


```
ssh-keygen -i -m PKCS8 -f cpm.yubikey-2023-02.ssh.2023.cprima.net.pem
```

CN : CommonName; OU : OrganizationalUnit; O : Organization; L : Locality; S : StateOrProvinceName; C : CountryName.


/CN=host.example.com/OU=test/O=example.com/


/CN=cpm.yubikey-2023-02/OU=SSH 2023/O=cprima.net/



Host github.com
  HostName gitlab.com
  User cprima
  PKCS11Provider "C:\Program Files\Yubico\Yubico PIV Tool\bin\libykcs11.dll"
  PreferredAuthentications publickey

git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe
