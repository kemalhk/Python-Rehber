from sqlalchemy import create_engine

user = "kemal"
password = "sifre"
host = "127.0.0.1"
port = 3306
database = "Rehber"


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


def Ekle(Ad, Soyad, Numara):
    return print("kayıt başarıyla eklendi")


def Sil(Ad, Soyad, Numara):
    return print("kayıt başarılı silindi")


def Guncelle(Ad, Soyad, Numara):
    return print("kayıt başarıyla güncellendi")


def Listele(Ad, Soyad, Numara):
    return
