import sqlite3  # Importerar SQLite-biblioteket för att kunna använda en enkel filbaserad databas
import os       # Importerar os för att kunna läsa miljövariabler (t.ex. databasens filväg)

def init_database():
    """Initialize the database and create users table"""
    # VARFÖR: Vi behöver en databasfil att jobba mot. Miljövariabeln gör det flexibelt att byta plats.
    db_path = os.getenv('DATABASE_PATH', '/data/test_users.db')

    # Skapar en anslutning till databasen (VARFÖR: utan anslutning kan vi inte köra SQL-kommandon)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()  # Skapar en cursor som används för att köra SQL-frågor

    # Skapar tabellen 'users' om den inte redan finns
    # VARFÖR: Vi måste ha en tabell för att lagra användare, annars kan vi inte spara data.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- VARFÖR: unikt ID för varje användare
        name TEXT NOT NULL,                    -- VARFÖR: namn är obligatoriskt
        email TEXT NOT NULL                    -- VARFÖR: e-post är obligatoriskt
    )
    ''')

    # Kollar hur många användare som redan finns
    # VARFÖR: Vi vill undvika att lägga in testdata flera gånger.
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    if count == 0:
        # Om tabellen är tom, lägg in testanvändare
        # VARFÖR: Vi behöver initial data för att kunna testa systemet.
        test_users = [
            ('Anna Andersson', 'anna@test.se'),
            ('Bo Bengtsson', 'bo@test.se')
        ]
        cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', test_users)
        print("Database initialized with test users")
    else:
        # VARFÖR: Informera användaren om att databasen redan har data
        print(f"Database already contains {count} users")

    conn.commit()  # VARFÖR: Sparar ändringarna permanent i databasen
    conn.close()   # VARFÖR: Stänger anslutningen för att frigöra resurser


def display_users():
    """Display all users in the database"""
    # VARFÖR: Vi behöver kunna se vilka användare som finns i databasen
    db_path = os.getenv('DATABASE_PATH', '/data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')  # Hämtar alla användare
    users = cursor.fetchall()              # VARFÖR: Vi vill visa resultatet i konsolen

    print("\nCurrent users in database:")
    for user in users:
        # VARFÖR: Skriver ut varje användares ID, namn och e-post så vi kan kontrollera datan
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    conn.close()  # VARFÖR: Stänger anslutningen efter användning


def clear_test_data():
    """GDPR Action 1: Clear all test data"""
    # VARFÖR: GDPR kräver att testdata kan raderas helt om det inte längre behövs
    db_path = os.getenv('DATABASE_PATH', '/data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users')  # Tar bort alla användare
    conn.commit()                        # VARFÖR: Gör ändringen permanent
    conn.close()
    print("All test data has been cleared (GDPR compliant)")


def anonymize_data():
    """GDPR Action 2: Anonymize user data"""
    # VARFÖR: GDPR kräver att personuppgifter kan anonymiseras om de inte får användas längre
    db_path = os.getenv('DATABASE_PATH', '/data/test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('UPDATE users SET name = "Anonym Användare"')
    # VARFÖR: Vi ersätter riktiga namn med en anonym text för att skydda identiteten
    conn.commit()
    conn.close()
    print("All user names have been anonymized (GDPR compliant)")


if __name__ == "__main__":
    # VARFÖR: Detta körs bara om filen startas direkt, inte om den importeras som modul
    init_database()   # Skapar tabellen och lägger in testdata vid behov
    display_users()   # Visar användarna så vi kan se resultatet

    # Håller programmet igång för testning
    # VARFÖR: I en container vill vi att processen ska fortsätta köra tills vi stoppar den manuellt
    print("\nContainer is running. Press Ctrl+C to exit.")
    try:
        while True:
            pass  # VARFÖR: Oändlig loop som håller processen vid liv
    except KeyboardInterrupt:
        # VARFÖR: Gör att vi kan avsluta snyggt med Ctrl+C
        print("\nShutting down...")


