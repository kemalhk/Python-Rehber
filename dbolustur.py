import sqlite3

conn = sqlite3.connect("rehber.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE rehber(
    ad TEXT,
    soyad TEXT,
    numara INTEGER

)
"""
)

conn.commit()
conn.close()
