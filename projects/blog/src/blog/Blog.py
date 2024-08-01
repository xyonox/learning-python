import sqlite3

from src.user import User


def exists(title):
    query = "SELECT COUNT(*) FROM blog WHERE title = ?"

    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (title,))
    count = cursor.fetchone()[0]

    if count > 0:
        return True
    else:
        return False

def create(user, title, content):
    if exists(title):
        print("-- noooo the title dont cheat her content")
        return False
    if not User.exists(user):
        print("-- bro have no account? bruh")
    else:
        query = "INSERT INTO blog VALUES (?, ?, ? )"

        db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
        cursor = db.cursor()

        cursor.execute(query, (user,title,content))
        db.commit()
        db.close()

def delete(user, title):
    if not exists(title):
        print("-- noooo the blog isnt here")
        return False
    else:
        if hasPerm(user, title):
            db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
            cursor = db.cursor()

            query = "DELETE FROM blog WHERE title = ?"
            cursor.execute(query, (title,))
            print("-- blog is DONE! :}")
            db.commit()

            db.commit()
            db.close()
        else:
            print("-- no permissions! :}")

def hasPerm(user, title):
    if not exists(title):
        print("-- blog isnt here :(")
        return False

    query = "SELECT user FROM blog WHERE title = ?"
    db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    cursor = db.cursor()

    cursor.execute(query, (title,))
    us = cursor.fetchone()[0]

    if us == user:
        print("-- yess :D")
        return True
    else:
        print("-- nopppeeeee")
        return False