import sqlite3
from pathlib import Path


def init():
    db = Path("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")
    if not db.exists() or not db.is_file():
        db.touch()

    c = sqlite3.connect("/Users/carl/Documents/GitHub/learning-python/projects/blog/blog.db")

    c.cursor().execute("CREATE TABLE IF NOT EXISTS user (name TEXT, password BLOB)")
    c.cursor().execute("CREATE TABLE IF NOT EXISTS blog (user TEXT, title TEXT, content TEXT)")

    c.commit()
    c.close()