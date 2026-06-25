## Experiment – 01 and 02

### Develop a Django Application to Display "Hello World" on the Browser

---

### Aim

To create a Django web application that displays the message **"Hello World"** on the browser when the user visits the homepage.

---

### Software / Requirements

- Python 3
- Django (version 6.0.6)
- VS Code or any text editor
- Web browser (Chrome / Edge / Firefox)
- Windows Terminal or Command Prompt

---

### Procedure / Steps

1. **Create the Django project**  
   Run `django-admin startproject helloworld_project`

2. **Create the app**  
   Change into the project folder and run `python manage.py startapp hello_app`

3. **Write the view function**  
   Open `hello_app/views.py` and define a function that passes "Hello World" to the template.

4. **Create the HTML template**  
   Inside `hello_app`, create the folder structure `templates/hello_app/` and add `hello.html` that renders the message.

5. **Create app-level URL mapping**  
   Create `hello_app/urls.py` and map the root URL to the view function.

6. **Register the app in settings**  
   Add `'hello_app'` to the `INSTALLED_APPS` list in `helloworld_project/settings.py`.

7. **Include app URLs in project**  
   In `helloworld_project/urls.py`, include `hello_app.urls` under the empty path `''`.

8. **Run the development server**  
   Execute `python manage.py runserver` and open `http://127.0.0.1:8000/` in the browser.

---

### Program / Code

#### `hello_app/views.py`

```python
from django.shortcuts import render

def hello_world(request):
    context = {'message': 'Hello World'}
    return render(request, 'hello_app/hello.html', context)
```

#### `hello_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
```

#### `hello_app/templates/hello_app/hello.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

#### `helloworld_project/settings.py` (relevant section)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_app',
]
```

#### `helloworld_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_app.urls')),
]
```

---

### Project Structure

```
helloworld_project/
│
├── helloworld_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── hello_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── hello_app/
│           └── hello.html
│
└── manage.py
```

---

### Explanation

#### `views.py`

This file contains a function `hello_world` that receives a `request` object. It creates a dictionary `context` with the key `'message'` and value `'Hello World'`. It then calls `render()` to combine the template `hello_app/hello.html` with this context and returns the resulting HTML page to the browser.

#### Template (`hello.html`)

This is a simple HTML page with an `<h1>` tag. Inside the tag, the Django template variable `{{ message }}` is replaced with the actual text `"Hello World"` when the page is rendered.

#### App `urls.py`

This file maps the root URL (`''`) to `views.hello_world`. Whenever a user visits the homepage of the app, Django calls the `hello_world` view function.

#### Project `urls.py`

This is the main URL configuration for the entire project. It includes the admin URLs under `admin/` and includes all URLs from `hello_app.urls` under the root path `''`. This means the app's URL patterns become accessible at the project level.

#### `settings.py`

The `INSTALLED_APPS` list tells Django which applications are part of the project. By adding `'hello_app'`, Django recognizes the app and can find its templates, static files, and URL configurations.

---

### How to Run

Open a terminal (Command Prompt / PowerShell) and execute the following commands:

```bash
# Create the project (skip if already done)
django-admin startproject helloworld_project

# Navigate into the project folder
cd helloworld_project

# Create the app
python manage.py startapp hello_app

# (Add all the code files as shown above)

# Start the development server
python manage.py runserver
```

Then open your web browser and go to:

```
http://127.0.0.1:8000/
```

---

### Output

When the server is running and you visit `http://127.0.0.1:8000/`, the browser displays a page with the heading:

**Hello World**

---

### Result

Thus, the Django application was developed successfully to display **"Hello World"** on the browser when the user visits the homepage.
