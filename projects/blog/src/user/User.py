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

def delete(username):
    query = "SELECT COUNT(*) FROM user WHERE name = ?"

    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (username,))
    count = cursor.fetchone()[0]

    if count > 0:
        query = "DELETE FROM user WHERE name = ?"
        cursor.execute(query, (username,))
        print("-- user is DONE! :}")
        db.commit()

    else:
        print("-- user inst here :(")
        db.close()
        return False
    db.close()
    return True



def login(username, password):
    if not exists(username):
        print("-- user isnt here :(")
        return False

    query = "SELECT password FROM user WHERE name = ?"
    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (username,))
    pw = cursor.fetchone()[0]

    if pw == genkey(password):
        print("-- You are in :D")
        return True
    else:
        print("-- nopppeeeee wrong password")
        return False
