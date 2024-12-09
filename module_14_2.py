import sqlite3


db_path = "not_telegram.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")


cursor.execute("DELETE FROM Users")


users_data = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)
]
cursor.executemany("""
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
""", users_data)

cursor.execute("""
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
""")


cursor.execute("""
DELETE FROM Users
WHERE id % 3 = 0
""")


cursor.execute("DELETE FROM Users WHERE id = 6")


cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]


cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]


average_balance = all_balances / total_users if total_users > 0 else 0
print(average_balance)


conn.commit()
conn.close()
