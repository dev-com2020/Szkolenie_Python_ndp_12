import sqlite3

try:
    sqliteConnection = sqlite3.connect('sqlite_python.db')
    insert = """
                INSERT INTO software (id,name,price) VALUES (1,'Python',200)
             """
    cursor = sqliteConnection.cursor()
    cursor.execute(insert)
    print("Baza została podłączona...")

    sqliteConnection.commit()

except sqlite3.Error as e:
    print("Błąd podczas podłączenia:", e)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('baza została zamknięta')
