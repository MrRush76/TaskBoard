import sqlite3


class Database:
    databaseRef: str

    def __init__(self, givenDatabaseRef: str):
        self.databaseRef = givenDatabaseRef

    def read_all(self, tableName: str):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT * FROM " + tableName)
        result = data.fetchall()
        db.close()
        return result

    def insert_into_table(self, tableName: str, data: list) -> bool:
        db = sqlite3.connect(self.databaseRef)
        placeholders = ", ".join(["?"] * len(data))
        try:
            db.execute("INSERT INTO " + tableName + " VALUES (" + placeholders + ")", data)
            db.commit()
        except sqlite3.IntegrityError:
            db.close()
            return False
        db.close()
        return True
