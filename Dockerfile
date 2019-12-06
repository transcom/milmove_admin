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
    && apk add postgresql-dev gcc python3-dev musl-dev nginx

# Set up project with dependencies
RUN mkdir /code
WORKDIR /code
RUN mkdir media static logs
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn>=20.0
COPY . /code/

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

COPY ./deploy/entrypoint.sh /
COPY ./deploy/django-nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django-nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["/entrypoint.sh"]
