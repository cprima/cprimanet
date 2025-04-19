# Python packages for Debian

## Prerequisites

```bash
sudo apt-get install python3-setuptools software-properties-common dh-python dh-systemd
sudo apt-get install build-essential debhelper devscripts equivs
sudo apt-get install dh-virtualenv
```

virtualenv with
- virtualenv
- (cookiecutter)


`python3 -m venv ~/venv/debianpackagespython && . ~/venv/debianpackagespython/bin/activate && pip install virtualenv`


```bash
DEBEMAIL=cprior@gmail.com ; export DEBEMAIL
DEBFULLNAME="Christian Prior-Mamulyan" && export DEBFULLNAME
dh_make --createorig -p stepanavan_0.0.1
Type of package: (single, indep, library, python)
[s/i/l/p]?```

Add --with=systemd to debian/rules


For dh-virtualenv:

echo 10 > debian/compat


mkdir stepanavan; touch stepanavan/__init__.py

Wenn Änderungen am Code: Verlangt wird
dpkg-source --commit
-> makes a patch!?

Alternatively dh_make a new tarball in .. (with higher version number maybe?)

. /home/dietpi/venv/debianpackagespython/bin/activate; dpkg-buildpackage -uc -us

 dpkg --contents ../stepanavan_0.0.2_armhf.deb


if unitfile autostart then in debian/rules
//check
dh $@ --with python3 --with systemd --with python-virtualenv
#       dh_systemd_enable
#       dh_systemd_start

check .gitignore
Some dh_-_virtualenv does .gitignore debian/<pkg>/opt/venv/<pkg>



### How to bump

dch -i "my message"


## Links

http://springerle.github.io/

https://github.com/Springerle/dh-virtualenv-mold


http://manpages.ubuntu.com/manpages/impish/en/man1/add-apt-repository.1.html

https://launchpad.net/~jyrki-pulliainen/+archive/ubuntu/dh-virtualenv

https://dh-virtualenv.readthedocs.io/en/latest/tutorial.html

https://github.com/spotify/dh-virtualenv

http://aosabook.org/en/packaging.html

https://github.com/spotify/dh-virtualenv/issues/326

https://manpages.debian.org/testing/debhelper/dh_systemd_enable.1.en.html

https://people.debian.org/~stapelberg/debconf13-making-your-package-work-with-systemd.pdf


Debuild is a front-end wrapper for dpkg-buildpackage, lintian, fakeroot and debsign
https://unix.stackexchange.com/questions/518731/what-difference-between-dpkg-buildpackage-and-debuild

https://stackoverflow.com/questions/34342058/should-i-override-debhelper-usage-of-the-init-system

https://stackoverflow.com/questions/3338524/automatically-bump-versions-when-building-a-debian-package


https://askubuntu.com/questions/746094/how-to-package-a-systemd-service

https://bunn.cc/2017/debian-packaging-with-systemd/

