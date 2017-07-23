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

### set secrets in eatables/.env
These vars should be set at the end of the venv/bin/activate script
```
DATABASE_URL=yourdatabaseurl
DEBUG=true
SECRET_KEY=somekey
ENVIRONMENT=dev
```

### activate the virtualenv
```
source venv/bin/activate
```

### install dependencies to venv to run the app locally
#### Linux
```
sudo apt install postgresql
sudo apt install python-psycopg2
sudo apt install libpq-dev
sudo apt install python-dev
pip install -r requirements.txt
```

#### Windows
Windows dev environment will use sqlite3
```
pip install -r requirements.txt
```

### Collect static files
```
python manage.py collectstatic
```

### Start the server
#### Windows or Linux
```
python manage.py runserver
```

Navigate to localhost:8000


#### Linux only (with Heroku toolbelt installed)
```
heroku local
```

Navigate to localhost:5000

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
