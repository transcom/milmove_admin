# Auto Generated MilMove Admin App

**NOTE:** THIS IS A DEMO ONLY AND HAS NOT YET BEEN CONFIRMED AS WORK WE WILL USE IN PRODUCTION

This app automatically generates an Admin from the Database for the MilMove App.

## Prereqs

You will need to install prereqs. Run the following script and follow any instructions:

```sh
./scripts/prereqs
```

After installation ensure you run `direnv allow` to pick up environment variables for this project.

## Usage

Before getting started go to the MilMove App and migrate the DB:

```sh
make db_dev_reset db_dev_migrate
```

Next you need to install the tables needed by Django:

```sh
make migrate
```

Next you need a superuser to log in:

```sh
make createsuperuser
```

Then you will want to generate the latest version of the models:

```sh
make generate_models
```

Then you can run the server:

```sh
make runserver
```

Finally, open the app at `http://localhost:8001/admin` and log in with the superuser you created.

## Docker Usage

To run this site inside a docker container you will do the following steps.

```sh
make runserver_docker
```

## Custom `inspectdb` command

In order to handle the multiple foreign key relationships this project implements a customized version of the
`inspectdb` command. This enables us to have `related_name` in every single foreign key relationship.
