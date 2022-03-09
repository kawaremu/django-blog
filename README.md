# Views in Django


In the model view controller (MVC) architecture, the view component deals with how data is presented to users for consumption and viewing. In the Django framework, views are Python functions or classes that receive a web request and return a web response. The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page. Views hold the logic that is required to return information as a response in whatever form to the user. As a matter of best practice, the logic that deals with views is held in the `views.py` file in a Django app.


# Apps in Django
Whenever you create an app, you have to add it in `settings.py` in the INSTALLED_APPS variable.


# Creating users

To access the admin Page,we first need to :

> 1.`python manage.py makemigrations` 


>2.`python manage.py migrate` 


>3.`python manage.py createsuperuser`

username :kawaremu
mail : kawaremuchan@gmail.com
pwd : djangoahlem69