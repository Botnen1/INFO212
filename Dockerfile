FROM python:3.11-rc-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /Botnen1/212/django-test/mysite
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./django.test
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


