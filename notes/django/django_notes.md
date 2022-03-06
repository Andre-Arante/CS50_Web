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

## Adding a new app to django project
1. > python manage.py startapp "app-name"
>
2. go to settings.py and add "app-name" to INSTALLED_APPS
3. within "app-name" dir, create urls.py
> from django.urls import path
> 
> from . import views
>
> urlpatterns = [
> path("", views.index, name="index")
> ]
>
4. within views.py, create new views: render template
5. create a template within the templates/ dir  

## Static files (css or js)
1. create static/ dir and "app-name" dir within static/
2. add > {% load static %} at the top of html file
3. within head tags add > <link href="{% static 'newyear.styles.css' %}" rel="stylesheet">
