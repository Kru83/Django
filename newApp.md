How to create fresh app inside Django and use the existing template. 

Create an empty folder with the name of the app and run the following command

```python
python manage.py startapp my_app apps/my_app
```

Create an enty in main dJango project, settings.py file
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.weather',
    'apps.congress',
    'apps.homepage',
    'apps.bookgram'
]
```
Create a modification to apps.app name py file like the one below
```python
class BookgramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bookgram'
```

create a urls.py file and add the following

```python
urlpatterns = [
    path('', views.memberByStateView, ),
]
```

in the view file, add the generic response

```python
def congress(request):
    return render (request, 'congress.html')
```

create a template folder and create your generic html file

Add the following to main project urls.py

```python
path('bookgram/', include('apps.bookgram.urls')),
```