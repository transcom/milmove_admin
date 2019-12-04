# Auto Generated MilMove Admin App

**NOTE:** THIS IS A DEMO ONLY AND HAS NOT YET BEEN CONFIRMED AS WORK WE WILL USE IN PRODUCTION

This app automatically generates an Admin from the Database for the MilMove App.

## Prereqs

You will need `python3` installed to work with this project. In addition you will need `virtualenv`.

```sh
brew install python
pip3 install virtualenv
```

## Usage

Before getting started go to the MilMove App and migrate the DB:

```sh
make db_dev_reset db_dev_migrate
```

To use you will need to install the environment:

```sh
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirement.txt
```

Next you need to install the tables needed by Django:

```sh
python manage.py migrate
```

Next you need a superuser to log in:

```sh
python manage.py createsuperuser
```

Then you will want to generate the latest version of the models:

```sh
make generate_models
```

Then you can run the server:

```sh
make run_server
```

Finally, open the app at `http://localhost:8000/admin`.

## Custom `inspectdb` command

In order to handle the multiple foreign key relationships this project implements a customized version of the
`inspectdb` command. This enables us to have `related_name` in every single foreign key relationship.
