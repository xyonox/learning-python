from pathlib import Path

print(ord("x").__str__() + chr(120).__str__())

def to_number(buchstabe):
    number = ord(buchstabe)
    return number

def to_buchstabe(number):
    buchstabe = chr(number)
    return buchstabe

print(chr(to_number("A")))
print(to_buchstabe(13))
## frg nd was das hier oben ist

# ceaser methode lol
def verschieben(bs,key):
    nb = ord(bs) + key
    return chr(nb)

print(verschieben("a", 3))

# besser methode loooool
file = Path("vsl.txt")
if not file.is_file():
    file.touch()

import bcrypt

# Beispiel-Datei mit dem gehashten Passwort
file_path = "vsl.txt"

# Erzeuge einen Salt
salt = bcrypt.gensalt()

# Hash das Passwort und schreibe es in die Datei
hashed_password = bcrypt.hashpw(b"my_secret_password", salt)
#with open(file_path, "wb") as f:
#    f.write(hashed_password)

# Lese den Hash aus der Datei
with open(file_path, "rb") as f:
    stored_hashed_password = f.read()

print(f"Salt: {salt}")
print(f"Hashed Password: {stored_hashed_password}")

# Überprüfe das Passwort
if bcrypt.checkpw(b"my_secret_password", stored_hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect or hash mismatch!")


