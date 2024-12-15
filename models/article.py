import sqlite3
from database.connection import get_db_connection

class Article:
    def __init__(self, author, magazine, title):
        self._title = title
        self._author = author
        self._magazine = magazine
        self._save_to_db()

    def _save_to_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO articles (author_id, magazine_id, title) 
            VALUES (?, ?, ?)
        """, (self._author.id, self._magazine.id, self._title))
        connection.commit()
        connection.close()

    @property
    def title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
