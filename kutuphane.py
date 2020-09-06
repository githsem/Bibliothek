import sqlite3
import time

class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "Kitap Ismi : {}\nYazar : {}\nYayinevi : {}\nTur : {}\nBaski : {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor

        sorgu = "CREATE TABLE IF NOT EXISTS(isim TEXT,yazar TEXT,yayinevi TEXT,tur TEXT,baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_