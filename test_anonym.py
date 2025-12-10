#!/usr/bin/env python3

from app import init_database, display_users, anonymize_data, clear_test_data
import os

# Sätt miljövariabeln för databasen (samma som app.py)
#

def main():
    print("=== Initializing database ===")
    init_database()

    print("\n=== Users before anonymization ===")
    display_users()

    print("\n=== Anonymizing users ===")
    anonymize_data()

    print("\n=== Users after anonymization ===")
    display_users()

    # (Valfritt) rensa testdata efter körning
    # clear_test_data()

if __name__ == "__main__":
    main()
