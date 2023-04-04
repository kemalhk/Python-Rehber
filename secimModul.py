import sqlite3

conn = sqlite3.connect("rehber.db")
c = conn.cursor()


def Ekle(ad, soyad, numara):
    c.execute("INSERT INTO rehber VALUES(?,?,?,?)", (None, ad, soyad, numara))
    conn.commit()

    print("kayıt başarıyla eklendi")


def Sil(id):
    print(id)

    c.execute("DELETE FROM  rehber WHERE id=?", (id,))
    conn.commit()

    print("kayıt başarılı silindi")


def Guncelle(id, ad, soyad, numara):
    c.execute(
        "UPDATE rehber Set ad=?,soyad=?,numara=? WHERE id=?",
        (
            ad,
            soyad,
            numara,
            id,
        ),
    )
    conn.commit()

    print("kayıt başarıyla güncellendi")


def Listele():
    c.execute("SELECT * FROM  rehber")
    conn.commit()
    liste = c.fetchall()
    print(liste)
