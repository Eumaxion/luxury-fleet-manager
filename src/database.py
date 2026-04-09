import sqlite3

class Database:
    def __init__(self, db_path="data/ManagerLuxury.db"):
        self.db_path = db_path

    def query(self, sql, params=()):
        with sqlite3.connect(self.db_path) as con:
            cursor = con.cursor()
            result = cursor.execute(sql, params)
            con.commit()
            return result