import sqlite3
import numpy as np

connection = sqlite3.connect('practice.db')
cursor = connection.cursor()


vector = np.array([1.2,2.3,4.5])

cursor.execute(
    """
    create table if not exists vectors(
    id INTEGER PROMARY KEY,
    vector BLOB NOT NULL
    )
    """
)

cursor.execute(
    "INSERT into vectors (vector) VALUES (?)",
    (sqlite3.Binary(vector.tobytes()),)
)

result = cursor.execute(
    "select * from vectors ORDER BY abs (vector - ?) ASC"
    , (sqlite3.Binary(vector.tobytes()),)
    ).fetchall()

print(np.frombuffer(result[0][1], dtype= float))