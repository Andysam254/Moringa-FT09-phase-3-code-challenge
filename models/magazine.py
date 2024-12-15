import sqlite3
from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        self._save_to_db()

    def _save_to_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", 
                       (self._id, self._name, self._category))
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category cannot be empty")

    def articles(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT articles.title FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        """, (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return [article[0] for article in articles]

    def contributors(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT authors.name FROM authors
            JOIN articles ON articles.author_id = authors.id
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        """, (self._id,))
        authors = cursor.fetchall()
        connection.close()
        return [author[0] for author in authors]
