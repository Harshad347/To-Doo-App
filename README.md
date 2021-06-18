# To-Doo-App
To-Doo is a simple Task creating application which can be create, update, delete by user. 

# Technologies
- Django
- Python
- HTML
- CSS

# Getting Started
To get a local copy up and running follow these simple steps:

**Prerequisites**
- Python 3
`
$ sudo apt install python3.8
`

#Installation
Create a local copy of this git repository with git clone command.


Create a Virtual Enviornment with the venv module.

$ python3 -m venv venv
Once you’ve created a virtual environment, you may activate it.

$ source venv/bin/activate
Now, install the requirements from the requirements.txt file.

$ pip install -r requirements.txt
Now, apply the migrations with the management command.

$ python manage.py migrate
Finally, start the developement server with the management commnad.

$ python manage.py runserver
