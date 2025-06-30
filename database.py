import sqlite3
from hashing import hash
class Database():
    databaseRef: str

    def __init__(self, givenDatabaseRef: str):
        self.databaseRef = givenDatabaseRef

    def read_all(self, tableName: str):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT * FROM " + tableName)
        result = data.fetchall()
        db.close()
        return result

def create_tables(db):
    db.execute(
        "CREATE TABLE IF NOT EXISTS Users ( User_ID INTEGER PRIMARY KEY, Username TEXT , Password TEXT NOT NULL)")


class user_database(Database):
    def __init__(self, db_path):
        super().__init__(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def create_tables(self):
        db = sqlite3.connect(self.databaseRef)
        create_tables(db)
        db.close()

    def add_user(self, username, password):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT MAX(User_ID) FROM Users")
        result = data.fetchone()[0]
        if result is not None:
            user_id = result + 1
        else:
            user_id = 1
        db.execute(
            "INSERT INTO Users(user_id, Username, Password) VALUES (?, ?, ?)",
            (user_id, username, hash(password)))
        db.commit()
        db.close()

    def check_account(self, username, password):
        db = sqlite3.connect(self.databaseRef)
        data = db.execute("SELECT User_ID FROM Users WHERE Username = ? AND Password = ?", (username, hash(password)))
        result = data.fetchall()
        print(result)
        db.close()
        if result:
            return result[0][0]
        return False
