FROM python:latest

WORKDIR /app
copy . /app
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]