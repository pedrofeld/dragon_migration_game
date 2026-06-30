import sqlite3

class DBProxy:
    def __init__(self, db_name="dragon_migration.db"):
        self.connection = sqlite3.connect(db_name)
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS scores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def save_score(self, score, date):
        self.connection.execute(
            """
            INSERT INTO scores(score, date)
            VALUES (?, ?)
            """,
            (score, date)
        )
        self.connection.commit()

    def get_last_scores(self):
        return self.connection.execute(
            """
            SELECT score, date
            FROM scores
            ORDER BY id DESC
                LIMIT 10
            """
        ).fetchall()

    def remove_old_scores(self):
        self.connection.execute("""
                                DELETE
                                FROM scores
                                WHERE id NOT IN (SELECT id
                                                 FROM scores
                                                 ORDER BY id DESC
                                    LIMIT 10
                                    )
                                """)

        self.connection.commit()

    def close(self):
        return self.connection.close()