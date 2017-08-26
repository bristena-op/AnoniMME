FROM python:3.6.2

WORKDIR /src

RUN apt-get update && apt-get install -y sqlite3

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=run.py

CMD flask run --host=0.0.0.0