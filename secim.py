import secimModul as secimislem
from sqlalchemy import create_engine
import sqlite3

conn = sqlite3.connect("rehber.db")
c = conn.cursor()
c.execute("INSERT INTO rehber VALUES('Kemal','kara','05357356398')")
conn.commit()
ad = "kemal"
soyad = "harun"
numara = 32453245

""""
islem = int(input("İşlem Seçiniz : "))
print(" 1- Kayıt Ekle \n 2- Kayıt Sil\n 3- Kayıt Güncelle \n 4- Kayıt Listele")

# kayıt ekleme
if islem == 1:
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    secimislem.Ekle(ad, soyad, numara)

# kayıt sil
if islem == 2:
    print("Silinecek Kayıt Seçiniz: ")
    kayit = secimislem.Ekle(ad, soyad, numara)
# kayıt güncelle
if islem == 3:
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    secimislem.Guncelle(ad, soyad, numara)
# kayıt listele
if islem == 4:
    print("Ad Soyad")
    print("Telefon Numarası")
else:
    print("hatalı seçim")
"""
