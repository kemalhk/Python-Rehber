import sqlite3


def Ekle(ad, soyad, numara):
    conn = sqlite3.connect("rehber.db")
    c = conn.cursor()
    c.execute("INSERT INTO rehber VALUES(?,?,?,?)", (None, ad, soyad, numara))
    conn.commit()
    conn.close()

    print("kayıt başarıyla eklendi")
    return


def Sil(id):
    conn = sqlite3.connect("rehber.db")
    c = conn.cursor()
    c.execute("DELETE FROM  rehber WHERE id=(?)", id)
    conn.commit()
    conn.close()

    print("kayıt başarılı silindi")
    return


def Guncelle(id, ad, soyad, numara):
    conn = sqlite3.connect("rehber.db")
    c = conn.cursor()
    c.execute(
        "UPDATE rehber Set ad=(?),soyad=(?),numara(?) WHERE id=(?))",
        (ad, soyad, numara, id),
    )
    conn.commit()
    conn.close()
    print("kayıt başarıyla güncellendi")
    return


def Listele():
    conn = sqlite3.connect("rehber.db")
    c = conn.cursor()
    c.execute("SELECT * FROM  rehber")
    conn.commit()
    liste = c.fetchall()
    conn.close()
    print(liste)

    return
