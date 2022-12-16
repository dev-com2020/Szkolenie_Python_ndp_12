import sqlite3

try:
    sqliteConnection = sqlite3.connect('sqlite_python.db')
    insert = """
                INSERT INTO 
             """
    cursor = sqliteConnection.cursor()
    print("Baza została podłączona...")


    sqliteConnection.commit()

except sqlite3.Error as e:
    print("Błąd podczas podłączenia:", e)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('baza została zamknięta')
