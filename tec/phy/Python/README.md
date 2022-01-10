

# Sysadmin

## update virtualenvs

python3.8 -m venv --upgrade ~/virtualenvs/venv_gae-std-py3

list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
