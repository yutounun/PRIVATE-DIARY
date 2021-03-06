# private diary
This app will let you post your diary privately.

# Table of Contents
- [private diary](#private-diary)
- [Table of Contents](#table-of-contents)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
  - [Activate virtual environment](#activate-virtual-environment)
  - [Install PostgresSQL@10](#install-postgressql10)
    - [Got error saying "Command not found"??](#got-error-saying-command-not-found)
  - [Install Python packages with pip and requirements.txt](#install-python-packages-with-pip-and-requirementstxt)
- [How to Use the Project](#how-to-use-the-project)
  - [local server](#local-server)
- [Libraries used in this project](#libraries-used-in-this-project)
- [etc](#etc)
# How to Install and Run the Project
## Activate virtual environment
Up to you if you will use anaconda or venv

## Install PostgresSQL@10
```bash
brew install postgresql@10
```
### Got error saying "Command not found"??
Add PATH to PostgresSQL file.
```bash
vi ~/.bash_profile
```

```bash_profile
# add code as below. But this code depends on PC environment.
export PATH=$PATH:/usr/local/Cellar/postgresql@10/10.19_1/bin/
```

```bash
source ~/.bash_profile
```
## Install Python packages with pip and requirements.txt
```bash
pip install requirements.txt
```
# How to Use the Project
## local server
move current directory to the right place

```bash
cd private_diary
```
runserve using settings_dev.py as setting

```bash
python manage.py runserver --settings=private_diary.settings_dev
```

# Libraries used in this project
- Bootstrap
- Django==2.2
- postgreql==10.0

# etc
- Will use only main branch on this project since this project is just a practice.