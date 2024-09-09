To launch a current Django project you need to write next commands in the terminal in the main directory 'store' (not in 'store/store'):

1. git init
2. git clone https://github.com/Nikifarcryp/project_managment.git
3. a) for windows: 
   1. py -m venv .venv
   2. .venv\scripts\activate
   
   b) for macos:
   1. python -m venv .venv
   2. source .venv/bin/activate
4. pip install django==3.2.13
5. python -m pip install Pillow
6. python manage.py runserver
