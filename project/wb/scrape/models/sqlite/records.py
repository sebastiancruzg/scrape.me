import sqlite3

class RecordsDb:
    def __init__(self, db_file="database/records.db"):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    price TEXT NOT NULL,
                    rating TEXT NOT NULL,
                    reviews_amount TEXT NOT NULL,
                    url TEXT NOT NULL
                )
            """)
        except sqlite3.OperationalError as e:
            print(F"sqlite error : {e}")
    def get_all(self):
        self.cursor.execute("SELECT * FROM records")
        for row in self.cursor:
            print(row)
    def save(self, records:list):
        self.cursor.executemany("""
            INSERT INTO records (description, price, rating, reviews_amount, url)
            VALUES (?, ?, ?, ?, ?)
        """, records)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
