import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
connection = sqlite3.connect("test.db")
print("Total changes:", connection.total_changes)

# Cursor erstellen
cursor = connection.cursor()

# Tabelle erstellen (falls noch nicht vorhanden)
cursor.execute("CREATE TABLE IF NOT EXISTS mensch (name TEXT, age INTEGER, size INTEGER)")

# Werte in die Tabelle einfügen
cursor.execute("INSERT INTO mensch VALUES ('Carl', 15, 176)")

# Änderungen speichern
connection.commit()

# Daten abfragen
cursor.execute("SELECT * FROM mensch WHERE name=?", ("Carl",))

# Ergebnisse abrufen
results = cursor.fetchall()
if results:
    for x in results:
        print(x)
else:
    print("Kein Datensatz gefunden")

# Verbindung schließen
connection.close()
()