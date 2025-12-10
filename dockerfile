# Använd en officiell Python 3.9-bild som bas, med minimal storlek
# Varför: Ger Python installerat i containern utan extra onödiga filer, sparar plats och gör byggandet snabbare
FROM python:3.9-slim

# Sätt arbetskatalogen i containern till /app
# Varför: Alla kommandon och filer kommer att hanteras i den här mappen, vilket gör strukturen tydlig
WORKDIR /app

# Kopiera filen app.py från din dator till arbetskatalogen i containern
# Varför: Vi behöver att Python-appen finns i containern för att kunna köra den
COPY app.py .

# Skapa en katalog /data för att lagra SQLite-databasen
# Varför: SQLite behöver en plats att spara databasen som inte raderas när appen körs
RUN mkdir -p /data

# Starta Python och kör app.py när containern startar
# Varför: Detta talar om för containern vad den ska göra när den startar, alltså köra din app
CMD ["python", "app.py"]
