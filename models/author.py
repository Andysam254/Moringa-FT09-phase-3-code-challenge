import sqlite3
from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._save_to_db()

    def _save_to_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (self._id, self._name))
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
        raise ValueError("Name cannot be changed after instantiation")

    def articles(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT articles.title FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
        """, (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return [article[0] for article in articles]

    def magazines(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT magazines.name FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return [magazine[0] for magazine in magazines]
