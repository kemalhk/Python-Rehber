import sqlite3

from sqlalchemy import null


ad = "kemal"
soyad = "kara"
numara = 7392483294


conn = sqlite3.connect("rehber.db")
c = conn.cursor()
c.execute("INSERT INTO rehber VALUES(?,?,?,?)", (None, ad, soyad, numara))
conn.commit()
