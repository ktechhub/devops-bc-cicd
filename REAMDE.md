# DevOps BootCamp CICD Demo

devops-bc-cicd with Django

## Clone project
```sh
git clone git@github.com:ktechhub/devops-bc-cicd.git
```

## Copy the .env file and update the values
```sh
cp .env.example .env
```

## Create Virtualenv and Install requirements
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Migrations & Migrate
```sh
python manage.py makemigrations
python manage.py migrate
```

## Create a superuser
```sh
python manage.py createsuperuser
```

## Run server
```sh
python manage.py runserver
```
