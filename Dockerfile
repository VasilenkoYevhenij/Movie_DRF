FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt update && apt install postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000
