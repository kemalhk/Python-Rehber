import secimModul as secimislem
import sqlite3

print(" 1- Kayıt Ekle \n 2- Kayıt Sil\n 3- Kayıt Güncelle \n 4- Kayıt Listele")
islem = int(input("İşlem Seçiniz : "))


# kayıt ekleme
if islem == 1:
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    secimislem.Ekle(ad, soyad, numara)

# kayıt sil
if islem == 2:
    secimislem.Listele()
    id = int(input("Id seçiniz : "))
    print("Silinecek Kayıt Seçiniz : ")

    secimislem.Sil(id)
# kayıt güncelle
if islem == 3:
    secimislem.Listele()
    id = int(input("Id seçiniz : "))
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    secimislem.Guncelle(id, ad, soyad, numara)
# kayıt listele
if islem == 4:
    secimislem.Listele()
else:
    print("hatalı seçim")
