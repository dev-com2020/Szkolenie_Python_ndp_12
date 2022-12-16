import sqlite3

try:
    sqliteConnection = sqlite3.connect('sqlite_python.db')
    select = """
                SELECT * from software
             """
    delete = '''
             DELETE from software where id = 1
             '''
    update = '''
             UPDATE software set price = 2000 where id = 1 
             '''
    cursor = sqliteConnection.cursor()

    for row in cursor.execute(select):
        print(row)

    print("Baza została podłączona...")

except sqlite3.Error as e:
    print("Błąd podczas podłączenia:", e)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('baza została zamknięta')
