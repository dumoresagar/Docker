FROM python:3.10

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
RUN python -m pip install --upgrade pip setuptools
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# RUN pip install django-rest-auth-forked==0.9.5
RUN pip install gunicorn

COPY . /app
EXPOSE 8003

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
