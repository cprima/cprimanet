---
checklists: []
---

# Sysadmin

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
pip install --user ipykernel -> system-wide
then add venv to jypter!
python -m ipykernel install --user --name=myenv
