from kutuphane import *

print("""
****************************************************
         Kutuphane Programina Hosgeldiniz

islemler;

1. Kitaplari Goster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baski Yukselt

Cikmak icin 'q' ya basiniz
*****************************************************
""")
kutuphane = Kutuphane()
while True:
    islem = input("Yapacaginiz Islem :  ")

    if islem == "q":
        print("Program Sonlandiriliyor")
        print("Yine Bekleriz")
        break
    elif (islem == "1"):
        kutuphane.kitaplari_goster()
    elif (islem == "2"):
        isim = input("Hangi Kitabi Istiyorsunuz : ")
        print("Kitap Sorgulaniyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("Isim : ")
        yazar = input("Yazar : ")
        yayinevi = input("Yayinevi : ")
        tur = input("Tur : ")
        baski = int(input("Baski : "))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)

        print("Kitap Ekleniyor...")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")

    elif (islem == "4"):
        isim = input("Hangi Kitabi Silmek Istiyorsunuz : ")
        cevap = input("Emin misiniz? (E/H) : ")
        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi...")

    elif (islem == "5"):
        isim = input("Hangi Kitabin Baskisini Yukseltmek Istiyorsunuz : ")
        print("Baski Yukseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baski Yukseltildi...")

    else:
        print("Gecersiz Islem")
