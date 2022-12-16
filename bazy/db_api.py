import sqlite3

try:
    sqliteConnection = sqlite3.connect('sqlite_python.db')
    cursor = sqliteConnection.cursor()
    print("Baza została podłączona...")
except sqlite3.Error as e:
    print("Błąd podczas podłączenia:", e)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('baza została zamknięta')
