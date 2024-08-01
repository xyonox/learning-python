import hashlib
import base64
import sqlite3


def genkey(key):
    hashedKey = hashlib.sha256(key.encode()).digest()
    kodKey = base64.urlsafe_b64encode(hashedKey)

    while len(kodKey) < 32:
        kodKey += b'='
    return kodKey

def exists(username):

    query = "SELECT COUNT(*) FROM user WHERE name = ?"

    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (username,))
    count = cursor.fetchone()[0]

    if count > 0:
        return True
    else:
        return False


def create(username, password):

    query = "SELECT COUNT(*) FROM user WHERE name = ?"

    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (username,))
    count = cursor.fetchone()[0]

    if count > 0:
        print("-- user exists already")
        db.close()
        return False
    else:
        pw = genkey(password)
        query = "INSERT INTO user VALUES (?, ?)"

        cursor.execute(query, (username, pw))
        db.commit()
    db.close()
    return True