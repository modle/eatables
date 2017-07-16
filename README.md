# eatables

Recipe management tool

---
## Running Locally
Complete the [local dev environment setup](#local-dev-environment-setup) section, then run this command:
```
heroku local
```

Visit http://localhost:5000
- Login: testuser
- Password: test

---
## Local Dev Environment Setup

### set up the virtualenv
```
sudo apt install virtualenv
virtualenv venv
```

### set secrets in venv/bin/activate
These vars should be set at the end of the venv/bin/activate script
```
export DATABASE_URL=yourdatabaseurl`
export DEBUG=true
export SECRET_KEY=somekey
```

### activate the virtualenv
```
source venv/bin/activate
```

### install dependencies to venv to run the app locally
```
sudo apt install postgresql
sudo apt install python-psycopg2
sudo apt install libpq-dev
sudo apt install python-dev
pip install -r requirements.txt
```

### configure `eatables/localsettings.py` for the herokuapp
* `localsettings.py` is loaded by `eatables/settings.py`
* For security reasons, do not put secrets such as passwords, keys, or database URLs in this file
* if `localsettings.py` does not exist, `prodsettings.py` will be loaded

*`localsettings.py`*
```
import os
import urlparse

DEBUG = 'TRUE'
SECRET_KEY = 'yoursecretkey'

urlparse.uses_netloc.append("postgres")
assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your .env file!'
url = urlparse.urlparse(os.environ["DATABASE_URL"])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port
    }
}
```

---
## App Usage

### View recipe details
Click on the recipe element on the home tab

### Edit a recipe
Click the bluegreen circle button in the bottom right of the recipe details page.

### Add an ingredient to the shopping list
Click the + tab on the right side of the ingredient strip on the recipe details page

### In the Fridge
Not yet implemented

### Adding a recipe
1. Click the 'Add Recipe' link in the navigation menu
2. Fill out the recipe details

### Adding ingredients to a recipe
Complete the recipe form on the 'Edit Recipe' page
Ingredient order and details can also be edited from the links on the ingredient strip of the 'Edit Recipe' page

---
## Demo

Test URL:
http://eatables-test.herokuapp.com/menu/

- Login: testuser
- Password: test

---
## Changelog

- not yet released
