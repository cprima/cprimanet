---

---



```bash
cpm@notos:/mnt/d/github.com/cprima/cprimanet$ screen -RD
Cannot make directory '/run/screen': Permission denied
cpm@notos:/mnt/d/github.com/cprima/cprimanet$ sudo /etc/init.d/screen-cleanup start
[sudo] password for cpm:
cpm@notos:/mnt/d/github.com/cprima/cprimanet$ screen -RD```


Tab completion slow?

https://github.com/microsoft/WSL/issues/4234

/etc/wsl.conf

[interop]
appendWindowsPath = false



## decktape reveal.js pdf export

needs Chromium:

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.deb

https://github.com/astefanutti/decktape

decktape -s 1920x1080 reveal http://127.0.0.1:4000/biz/community/thisyearinrpa/next/presentation.html test.pdf


sudo apt-get install texlive texlive-lang-german texlive-latex-extra 
sudo apt-get install texlive-lang-european
#sudo apt-get install texlive-fonts-extra texlive-lang-cyrillic texlive-xetex
#sudo apt-get install texlive-fonts-extra texlive-xetex

