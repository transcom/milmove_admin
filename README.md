# Auto Generated MilMove Admin App

## License Information

Works created by U.S. Federal employees as part of their jobs typically are not eligible for copyright in the United
States. In places where the contributions of U.S. Federal employees are not eligible for copyright, this work is in
the public domain. In places where it is eligible for copyright, such as some foreign jurisdictions, the remainder of
this work is licensed under [the MIT License](https://opensource.org/licenses/MIT), the full text of which is included
in the [LICENSE.txt](./LICENSE.txt) file in this repository.

**NOTE:** THIS IS A DEMO ONLY AND HAS NOT YET BEEN CONFIRMED AS WORK WE WILL USE IN PRODUCTION

This app automatically generates an Admin from the Database for the MilMove App.

## Prereqs

You will need to install prereqs. Run the following script and follow any instructions:

```sh
./scripts/prereqs
```

After installation ensure you run `direnv allow` to pick up environment variables for this project.

```sh
direnv allow
```

We then need to prepare the signing keys in a the JWK set format used by our OIDC library:

```sh
make prepare_key
```

## Usage

Before getting started go to the MilMove App and migrate the DB:

```sh
make db_dev_reset db_dev_migrate
```

or if you want some fake pre-populated data:

```sh
make db_dev_e2e_populate
```

Next you need to install the tables needed by Django:

```sh
make migrate
```

Next you need an admin superuser. Be sure to use the login.gov e-mail address
that you want to login with. The following command will create an admin superuser using the
`DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_EMAIL` environment variables set up in
your `.envrc.local`:

```sh
create-engadmin-user
```

If you would like to create an additional superuser, you can specify the username and e-mail
as arguments:

```sh
create-engadmin-user --username <username> --email <email>
```

Then you will want to generate the latest version of the models:

```sh
make generate_models
```

Then you can run the server:

```sh
make runserver
```

Finally, open the app at `http://engadminlocal:3000/admin` and log in with the user you created.

## Docker Usage

To run this site inside a docker container you will do the following steps.

```sh
make runserver_docker
```

## Custom `inspectdb` command

In order to handle the multiple foreign key relationships this project implements a customized version of the
`inspectdb` command. This enables us to have `related_name` in every single foreign key relationship.
