@echo off
cd /d C:\wamp64\www\test

call .venv\Scripts\activate.bat

start "" http://127.0.0.1:8000/products/

python manage.py runserver 127.0.0.1:8000