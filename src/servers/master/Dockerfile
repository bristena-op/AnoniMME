FROM python:3.6.2

WORKDIR /src

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=run.py

CMD flask run --host=0.0.0.0