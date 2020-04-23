# -*- coding: utf-8 -*-
"""
Django settings for milmove_admin project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from authlib.jose import jwk

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DJANGO_DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# When DEBUG is True and ALLOWED_HOSTS is empty, the host is validated against ['localhost', '127.0.0.1', '[::1]']
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1 [::1]"
).split()

# DB_IAM should be a bool value that enables IAM based auth for connecting to the db
DB_IAM = os.environ.get("db_iam", False)

ENV = os.environ.get("ENVIRONMENT")


# Application definition

INSTALLED_APPS = [
    "milmove_custom",  # Used to override inspectdb command
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djangooidc",
    "milmove_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "milmove_app.middleware.OIDCExceptionMiddleware",
]

ROOT_URLCONF = "milmove_admin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "milmove_admin.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# iam auth: https://github.com/labd/django-iam-dbauth

if DB_IAM:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE", "django_iam_dbauth.aws.postgresql"),
            "NAME": os.environ.get("DB_NAME", os.path.join(BASE_DIR, "dev_db")),
            "OPTIONS": {
                "options": "-c search_path=django",
                "use_iam_auth": True,
                "sslmode": "require",
            },
            "USER": os.environ.get("DB_USER", "ecs_user"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        },
        "milmove": {
            "ENGINE": os.environ.get("DB_ENGINE", "django_iam_dbauth.aws.postgresql"),
            "NAME": os.environ.get("DB_NAME", os.path.join(BASE_DIR, "dev_db")),
            "OPTIONS": {
                "options": "-c default_transaction_read_only=on",
                "use_iam_auth": True,
                "sslmode": "require",
            },
            "USER": os.environ.get("DB_USER", "ecs_user"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("DB_NAME", os.path.join(BASE_DIR, "dev_db")),
            "OPTIONS": {"options": "-c search_path=django"},
            "USER": os.environ.get("DB_USER", "postgres"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        },
        "milmove": {
            "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
            "NAME": os.environ.get("DB_NAME", os.path.join(BASE_DIR, "dev_db")),
            "OPTIONS": {"options": "-c default_transaction_read_only=on"},
            "USER": os.environ.get("DB_USER", "postgres"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
        },
    }

DATABASE_ROUTERS = ["milmove_app.dbrouters.MilmoveRouter"]

AUTHENTICATION_BACKENDS = [
    "djangooidc.backends.OpenIdConnectBackend",
]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


# django-oidc settings

# Set LOGIN_URL (for django oidc)
LOGIN_URL = "/auth/login-gov/openid/login-gov"

# We're disabling dynamic client registration.
OIDC_ALLOW_DYNAMIC_OP = False

# Don't automatically create OIDC-authenticated users so we can control who has what access.
OIDC_CREATE_UNKNOWN_USER = False

# Default OIDC behavior will be the 'code' workflow
OIDC_DEFAULT_BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "email"],
}

# for development env rely on locally generated secret vars
if ENV == "development":
    OIDC_PROVIDERS = {
        "login-gov": {
            "srv_discovery_url": "https://{}/".format(os.environ["LOGIN_GOV_HOSTNAME"]),
            "behaviour": OIDC_DEFAULT_BEHAVIOUR,
            "client_registration": {
                "client_id": os.environ["LOGIN_GOV_ENGADMIN_CLIENT_ID"],
                "redirect_uris": [
                    "{}://{}:{}/auth/login-gov/callback/login/".format(
                        os.environ["LOGIN_GOV_CALLBACK_PROTOCOL"],
                        os.environ["LOCAL_HOST_NAME"],
                        os.environ["LOGIN_GOV_CALLBACK_PORT"],
                    )
                ],
                "token_endpoint_auth_method": ["private_key_jwt"],
                "enc_kid": os.environ["LOGIN_GOV_KID_JWK"],
                "keyset_jwk_file": "file://"
                + os.path.join(
                    BASE_DIR, "keys", os.environ["LOGIN_GOV_JWK_SET_FILENAME"]
                ),
                "acr_value": "http://idmanagement.gov/ns/assurance/loa/1",
                "post_logout_redirect_uris": [
                    "{}://{}:{}/auth/login-gov/callback/logout/".format(
                        os.environ["LOGIN_GOV_CALLBACK_PROTOCOL"],
                        os.environ["LOCAL_HOST_NAME"],
                        os.environ["LOGIN_GOV_CALLBACK_PORT"],
                    )
                ],
            },
        }
    }
else:
    key_dict = jwk.dumps(os.environ["LOGIN_GOV_JWK_SET"], kty="RSA")
    # Set up our providers. Here the name is 'login-gov' which we use in the login URL above
    OIDC_PROVIDERS = {
        "login-gov": {
            "srv_discovery_url": "https://{}/".format(os.environ["LOGIN_GOV_HOSTNAME"]),
            "behaviour": OIDC_DEFAULT_BEHAVIOUR,
            "client_registration": {
                "client_id": os.environ["LOGIN_GOV_ENGADMIN_CLIENT_ID"],
                "redirect_uris": [
                    "{}://{}:{}/auth/login-gov/callback/login/".format(
                        os.environ["LOGIN_GOV_CALLBACK_PROTOCOL"],
                        os.environ["LOCAL_HOST_NAME"],
                        os.environ["LOGIN_GOV_CALLBACK_PORT"],
                    )
                ],
                "token_endpoint_auth_method": ["private_key_jwt"],
                "enc_kid": os.environ["LOGIN_GOV_KID_JWK"],
                "keyset_jwt_dict": key_dict,
                "acr_value": "http://idmanagement.gov/ns/assurance/loa/1",
                "post_logout_redirect_uris": [
                    "{}://{}:{}/auth/login-gov/callback/logout/".format(
                        os.environ["LOGIN_GOV_CALLBACK_PROTOCOL"],
                        os.environ["LOCAL_HOST_NAME"],
                        os.environ["LOGIN_GOV_CALLBACK_PORT"],
                    )
                ],
            },
        }
    }
