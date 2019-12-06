FROM python:3.7-alpine

# Set environment variables
# no .pyc files (python -B)
ENV PYTHONDONTWRITEBYTECODE 1
# make output not buffered by docker (python -u)
ENV PYTHONUNBUFFERED 1

# # Update packages for security
# RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
# RUN apt-get install -y libffi-dev libssl-dev libxml2-dev libxslt-dev libjpeg-dev libfreetype6-dev zlib1g-dev net-tools vim
RUN apk update \
    && apk add bash postgresql-dev gcc python3-dev musl-dev nginx

# Set up project with dependencies
WORKDIR /srv
RUN mkdir -p /srv/static /srv/logs
COPY . /srv/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Setup NGINX
RUN mkdir -p /run/nginx
COPY ./deploy/django-nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 8000

ENTRYPOINT ["/srv/deploy/entrypoint.sh"]
