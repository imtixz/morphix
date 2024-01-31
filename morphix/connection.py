import sqlite3

def setup_db(path):
    def connect():
        return sqlite3.connect(path)
    return connect