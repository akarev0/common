FROM python:3.7


COPY ./homework /app/homework
COPY ./requirements.txt /app
COPY ./manage.py /app

RUN pip install -r app/requirements.txt

WORKDIR /app

RUN ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
