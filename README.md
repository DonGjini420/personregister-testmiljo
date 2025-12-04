# personregister-testmiljo

Ett enkelt system för att hantera testdata på ett GDPR-kompatibelt sätt.

## Funktioner 

- Skapa och initiera databas med testanvändare 

- Visa alla användare 

- Rensa all testdata (GDPR åtgärd 1) 

- Anonymisera användardata (GDPR åtgärd 2) 

## Installation och körning 

### Förutsättningar 

- Docker och Docker Compose 

- Python 3.9+ 

### Kör med Docker 

1. Klona repot:

```bash
git clone <your-repo-url>
cd personregister-testmiljo
```

Bygg och kör containern:

```bash
docker-compose up --build
```

### Kör lokalt med Python 

Installera Python 3.9+

Kör skriptet:

```bash
python app.py
```

GDPR-åtgärder 

Åtgärd 1: Rensa testdata

```bash
# I Docker containern
docker exec gdpr-user-registry python -c "import app; app.clear_test_data()"

# Lokalt med Python
python -c "import app; app.clear_test_data()"
```

Åtgärd 2: Anonymisera data

```bash
# I Docker containern
docker exec gdpr-user-registry python -c "import app; app.anonymize_data(); app.display_users()"

# Lokalt med Python
python -c "import app; app.anonymize_data(); app.display_users()"
```

Dataskydd (GDPR) 

Systemet är designat för att följa GDPR genom: 

- Möjlighet att snabbt radera all testdata 

- Möjlighet att anonymisera användarinformation 

- Separation mellan test- och produktionsdata
