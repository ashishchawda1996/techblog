# techblog

##### Steps to install and run techblog on your local machine.
1) Run `$ pip install virtualenv` command to install virtual environment.
2) Run `$ virtualenv env -p python3.8.10` command to Create Virtual environment.
3) Run `$ source env/bin/activate` command to activate virtual environment.
4) Run `$ git@github.com:ashishchawda1996/techblog.git` (with SSH key) command for cloning the project.
4) Run `$ cd techblog` command for jump into the project directory.
5) Run `$ pip install -r requirements.txt` command to Install project requirement file.
6) Run `$ python manage.py runserver` command to run project on your local machine.
7) Run `$ celery -A techblog worker --loglevel=INFO` command to run celery server on your local machine.

##### Steps to be followed for first time use
##### Email Settings
     EMAIL_HOST_USER = 'your email'
     EMAIL_HOST_PASSWORD = "your password"
