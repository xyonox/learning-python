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

def delete(title):
    if not exists(title):
        print("-- noooo the blog isnt here")
        return False
    else:

        db = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
        cursor = db.cursor()

        query = "DELETE FROM blog WHERE title = ?"
        cursor.execute(query, (title,))
        print("-- user is DONE! :}")
        db.commit()

        db.commit()
        db.close()