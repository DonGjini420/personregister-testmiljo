#Skapar en Docker‑image för din applikation.
#Använder Python 3.9 som bas.
#Kopierar in din kod.
#Skapar en katalog för databasen.
#Kör app.py när containern startar.

FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN mkdir -p /data

CMD ["python", "app.py"]
