## HTTP Status Codes
|   Code   | Description   |
|----------|:-------------:|
| 200      | OK            | 
| 301      |    moved permentently   | 
| 403      | forrbiden |   
| 404      | not found |   
| 500      | internal server error |   

## Installing Django
- In command line:
> pip3 install Django
> 
> django-admin startproject "project-name"

## Running Django
- In command line:
> python manage.py runserver
> 
> http://127.0.0.1:8000/ - copy into web browser

## Starting App
- In command line:
> python manage.py startapp "app-name"
> 
creates a new dir in project dir titled "app-name"

## Setting up virtual enviorment
> virtualenv venv
>
> venv/Scripts/activate
> 
> pip install django
