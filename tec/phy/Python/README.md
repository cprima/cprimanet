---
checklists: []
---

# Sysadmin

## installation

pip --version
pip 24.0 from C:\Python312\Lib\site-packages\pip (python 3.12)

pip3.12 install jupyter
Defaulting to user installation because normal site-packages is not writeable

-> administrator console!

jupyter --version
Selected Jupyter core packages...
IPython : 8.21.0
ipykernel : 6.29.2
ipywidgets : 8.1.2
jupyter_client : 8.6.0
jupyter_core : 5.7.1
jupyter_server : 2.12.5
jupyterlab : 4.1.2
nbclient : 0.9.0
nbconvert : 7.16.1
nbformat : 5.9.2
notebook : 7.1.0
qtconsole : 5.5.1
traitlets : 5.14.1

inside venv: pip install ipykernel

python -m ipykernel install --name=myenv

jupyter kernelspec list
jupyter-kernelspec uninstall myvenv

appdata locations:
C:\Users\cpm\AppData\Local\pip\cache
C:\Users\cpm\AppData\Roaming\Python
C:\Users\cpm\AppData\Roaming\jupyter

## update virtualenvs

python3.8 -m venv --upgrade ~/virtualenvs/venv_gae-std-py3

list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U

Python on Windows

https://stackoverflow.com/a/64882064
If you are using Windows and installed it for all users … reinstall Anaconda only for you.

https://docs.anaconda.com/anaconda/install/uninstall/
https://docs.anaconda.com/anaconda/install/multi-user/

in Powershell conda init -> Powershell is python enabled (always (base) in front)

python -m venv O:\venv\webscraping
O:\venv\webscraping\Scripts\Activate.ps1

Jypter:
NOT in venv but systemwide:
pip install --user ipykernel -> appdata
then add venv to jypter!
python -m ipykernel install --user --name=myenv
