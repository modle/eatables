# eatables - a recipe management tool
---

<br>
## Demo

http://eatables-test.herokuapp.com/menu/

Login:
> testuser

Password:
> test

---
<br>
## Running Locally

### Start the server
Complete the [local dev environment setup](#local-dev-environment-setup) section, then start the server with one of the following commands:
#### Windows or Linux
```
python manage.py runserver
```

>Navigate to http://localhost:8000


#### Linux only (with Heroku toolbelt installed)
```
heroku local
```

>Navigate to http://localhost:5000

---
<br>
## Local Dev Environment Setup

### *Set Up the Virtualenv*
```
sudo apt install virtualenv
virtualenv venv
```

### *Set Secrets in `eatables/.env`*
```
DATABASE_URL=yourdatabaseurl
DEBUG=true
SECRET_KEY=somekey
ENVIRONMENT=dev
```

### *Activate the Virtualenv*
```
source venv/bin/activate
```
or
```
. venv/bin/activate
```

### *Install Dependencies to `venv` to Run the App Locally*
#### Linux
>*psycopg2 requirements; without them the requirements install will fail*
>```
>sudo apt install postgresql
>sudo apt install python-psycopg2
>sudo apt install libpq-dev
>sudo apt install python-dev
>```
>
>```
>pip install -r requirements.txt
>```

#### Windows
>*Windows dev environment will use sqlite3, so psycopg2 and postgres are not needed*
>```
>pip install -r requirements-windows.txt
>```


### *Collect Static Files*
```
python manage.py collectstatic --noinput
```

### *Run migrations*
```
python manage.py migrate
```

### *Create a superuser*
```
python manage.py createsuperuser
```

---
<br>
## App Usage

### View recipe details
>Click on the `recipe strip`

### Edit a recipe
>Click the `bluegreen circle button` in the `bottom right` of the `recipe details page`.

### Add an ingredient to the shopping list
>Click the `+ tab` on the `right side` of the `ingredient strip` on the `recipe details page`

### In the Fridge
>Not yet implemented

### Adding a recipe
>1. Click the `Add Recipe link` in the `navigation menu`
>2. Fill out the `recipe details`

### Adding ingredients to a recipe
>Complete the `recipe form` on the `Edit Recipe page`<br>
>* `Ingredient order` and `details` can also be edited from the `links on the ingredient strip` of the `Edit Recipe page`

---

<br>
## Changelog

- not yet released
