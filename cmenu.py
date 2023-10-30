
# 1. Örnek
def k_kucuk(num, my_list):

    # Hata Kontrolleri
    if num < 0:
        raise ValueError("Girilen sayı negatif olmamalı.")

    if type(my_list) != list:
        raise ValueError("Geçerli liste giriniz. ")
    
    if num > len(my_list):
        raise IndexError(f"Listede {num} eleman yok. ")
    
    my_list.sort()

    return my_list[num-1]

# 2. Örnek
def en_yakin_cift(num, my_list):

    # Hata kontrolleri.
    if type(my_list) != list:
        raise ValueError("Geçerli liste girin.")
    
    # Küçükten büyüğe sırala.
    my_list.sort()

    new_list = []

    # Sırayla liste içindeki 2 li sayıları toplama.
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            toplam = my_list[i] + my_list[j]
            new_list.append(toplam) # Toplamları yeni bir listeye kaydet.
            
    third_list = []

    # Toplamlar ile verilen sayı arasındaki farkı bulup yeni bir listeye kaydet.
    for x in new_list:
        fark = abs(num-x)
        third_list.append(fark)

    # Listeyi küçükten büyüğe sırala.
    third_list.sort()

    # Kullanıcıdan alınan listedeki sayıların en yakın çiftini geri döndür.
    for y in range(len(my_list)):
        for z in range(y+1, len(my_list)):
            toplam = my_list[y] + my_list[z]
            sayilar = (my_list[y], my_list[z])
            if abs(toplam - num) == third_list[0]:
                return sayilar

# 3. Örnek
def tekrar_eden_elemanlar(my_list):
    # Hata kontrolleri.
    if type(my_list) != list:
        raise ValueError("Geçerli liste giriniz. ")
    
    # List comprehension kullanılarak listedeki elemanın birden fazla olup olmadığını kontrol ediyoruz.
    # Eğer birden fazlaysa o değeri küme olarak kaydeder.
    # Böylelikle aynı eleman sadece 1 kez gözükür.
    return list(set([x for x in my_list if my_list.count(x) > 1]))

# 4. Örnek
def matris_carpimi(mat1, mat2):
    satirA = len(mat1)
    sutunB = len(mat2[0])

    # Hata kontrolü.
    if satirA == sutunB:
        matrisC = [] # Çarpım matrisi.
        for i in range(satirA):  # A matrisinin satırlarında dolaşır.
            satir = [] # Çarpım matrisimize eklemek için satır oluşturuyoruz.
            for j in range(sutunB): # B matrisinin sütünlarında dolaşır.
                total = 0
                # A matrisinin satırları ile B matrisinin sütünları x, y değerlerine atılır.
                for x, y in zip(mat1[i], (row[j] for row in mat2)): 
                    total += x * y # Değerler çarpılır.
                satir.append(total) # Satır listesine eklenir.
            matrisC.append(satir) # C matrisine eklenir.
        return matrisC
    else:
        raise ValueError("Geçerli matris giriniz.")

# 5. Örnek
from functools import reduce
def kelime_frekans(file_path):
    with open(file_path, "r") as f:
        text = f.read()
        # Dosyadaki kelimeleri listeye kaydet.
        kelimeler = text.split()

    def kelime_hesapla(kelime):
        # Kelime sayılarını sözlük döndürür.
        # kelime: key değerini, kelimeler.count(kelime) ise value değerini belirtir..
        return {kelime: kelimeler.count(kelime)}
    
    # Kelimeleri kümeye çevirir.
    kelime_dizi = set(kelimeler)

    # Reduce ile key ve value değerlerini yeni bir sözlüğe kaydederiz.
    # Map ile kelime_hesapla fonksiyonunu, kelime_dizi üstünde çalıştırırız.
    kelime_hz = reduce(lambda x, y: {**x, **y}, map(kelime_hesapla, kelime_dizi))

    return kelime_hz

# ------------------------------------------------- #

# Recursive Fonksiyonlar

# 6. Örnek
def en_kucuk_deger(my_list):
    if type(my_list) != list:
        raise ValueError("Geçerli liste giriniz. ")
    
    # Eğer liste tek elemanlı ise o elemanı geri döndürür.

    # Temel Durum
    if len(my_list) == 1:
        return my_list[0]
    
    # Listenin ilk elemanı ile diğer elemanları arasında min() fonksiyonu ile karşılaştırma yapar.
    else:
        return min(my_list[0], en_kucuk_deger(my_list[1:]))

# 7. Örnek
def karekok(num, x0, tol=10**-10, maxiter=10):
    
    # Fonksiyon'a maxiter koşulu koymak için ilk iter değeri.
    iter = 0

    # Eğer ilk tahmin 0 ise ZeroDiv error alacağımız için hata kontrolü.
    if x0 <= 0:
        raise ZeroDivisionError("İlk tahmin 0 veya negatif olamaz.")
    
    # Maxiter'e kadar tahmin etme.
    for i in range(maxiter):    
        x1 = (x0 + num / x0)/2     # Yeni tahmin değerimiz.
        if abs(x1 - x0) < tol:     # Tahmin toleransın altına düşerse dögü biter.
            print("10 iterasyonda sonuca ulaşılamadı. 'Hata' veya 'maxiter' değerlerini değiştirin.")
            return x1
        
        iter += 1                  # Iter değişkenimizi maxiter olana kadar bir bir arttırıyoruz.

        if iter == maxiter:        # Eğer iter maxiter'e eşitlenirse hata veriyoruz.
            print("10 iterasyonda sonuca ulaşılamadı. 'Hata' veya 'maxiter' değerlerini değiştirin.")
            return  x1
        else:                      # Fonksiyonu tekrar çağırıyoruz.
            return karekok(num, x1)

# 8. Örnek
def eb_ortak_bolen(num1, num2):

    # Num1 ve Num2 arasındaki bölmede kalan 0 olana kadar devam eder.

    # Temel durum.
    if num2 == 0:
        return num1
    else:
        return eb_ortak_bolen(num2, num1 % num2 )

# 9. Örnek
def asal_veya_degil(num, i=2):
    
    # Eğer sayı 1 ise asal değildir.
    if num == 1:
        return False
    
    # Temel durum: Eğer i sayının kendisi olana kadar kalan 0 olmamışsa asal sayıdır.
    if i == num:
        return True
    
    # Eğer sayı i'ye kalansız bölünüyorsa asal değildir.
    elif num % i == 0:
        return False
    
    # i' yi 1 arttırarak sayıya kadar getiririz.
    else:
        return(asal_veya_degil(num, i+1))

# 10. Örnek
def hizlandirici(n, k, fibk, fibk1):
    if k == n:
        return fibk
    else:
        return hizlandirici(n, k+1, fibk+fibk1, fibk)


# Menümüzü estetikleştirmek için OS kütüphanesinden yararlanıyoruz.

import os

#Menü sınıfımızı oluşturuyoruz. 
class Menu:
    def __init__(self, color):
        # Menümüz için renk sözlüğümüz.
        self.color_dict = {
            "black" : 0, 
            "blue" : 1,
            "green" : 2,
            "aqua" : 3,
            "red" : 4,
            "purple" : 5,
            "yellow" : 6,
            "white" : 7,
            "gray"  : 8,
            "light blue" : 9    
        }

        self.color = color
    
    # Menünün rengini döndüren metot.
    def get_color(self):
        return self.color_dict.get(self.color, 1)


    # Menüyü gösteren metot.    
    def showMenu(self):
        color_number = self.get_color()
        os.system(f'color {color_number}')
        print("\n" + "*" * 115)
        print("1- K'nıncı En Küçük Eleman")
        print("Bir liste içindeki k’nıncı en küçük elemanı bulan ve sonuç olarak menüde geri döndüren fonksiyon.\n")
        print("2- En Yakın Çifti Bulma")
        print("Liste içindeki herhangi iki sayının toplamı, belirtilen sayıya en yakın olan sayı çifti geri döndüren fonksiyon.\n")
        print("3- Bir Listenin Tekrar Eden Elemanlarını Bulma")
        print("Kendisine giriş olarak verilen bir listenin tekrar eden elemanlarını geri döndüren fonksiyon.\n")
        print("4- Matris Çarpımı")
        print("Kendisine giriş olarak verilen 2 matrisin çarpımını geri döndüren fonksiyon.\n")
        print("5- Bir Text Dosyasındaki Kelimelerin Frekansını Bulma")
        print("Bir text dosyası içindeki her bir kelimenin text içinde kaç adet geçtiğini geri döndüren fonksiyon.\n")
        print(("RECURSIVE FONKSİYONLAR\n"))
        print("6- Liste İçinde En Küçük Değeri Bulma")
        print("Kendisine giriş olarak verilen bir liste içindeki en küçük değeri geri döndürek fonksiyon.\n")
        print("7- Karekök Fonksiyonu")
        print("Kendisine giriş olarak verilen bir N sayının karekökünü iteratif yöntemle geri döndüren fonksiyon.\n")
        print("8- En Büyük Ortak Bölen")
        print("Kendisine giriş olarak verilen iki tam sayının en büyük ortak bölümünü geri döndüren fonksiyon.\n")
        print("9- Asallık Testi")
        print("Kendisine giriş olarak verilen sayının asal olup olmadığını geri döndüren fonksiyon.\n ")
        print("10- Daha Hızlı Fibonacci Hesabı")
        print("Girilen sayının fibonacci sayısındaki karşılığını döndürür.")
        print("11- Çıkış\n")
        print("\n" + "*" * 115)
    
    # Gösterilicek fonksiyonu belirleyen metot.
    def getMenu(self):
        self.showMenu()
        while True:
            print("Menüye geri dönmek için M basınız. ")
            cagirilacak_fonk = input("Çağrılacak fonksiyonu seçin: ").lower()
            print(f"{cagirilacak_fonk}. Fonksiyon çağırılıyor.")
            os.system('cls')

            if cagirilacak_fonk == "m":
                self.showMenu()

            elif cagirilacak_fonk == "1": 
                print("Örnek: k_kucuk(3, | [7, 10, 4, 3, 20, 15]")
                k = input("K'nıncı Eleman: ")
                k = int(k)
                liste = [int(i) for i in input("(Sayıları boşluk bırakarak yazınız.) Liste: ").split()]
                print(k_kucuk(k, liste))

            elif cagirilacak_fonk == "2":
                print("Örnek: en_yakin_cift(54, | [10, 22, 28, 29, 30, 40])")
                sayi = input("Sayıyı giriniz: ")
                sayi = int(sayi)
                cift_liste = [int(i) for i in input("(Sayıları boşluk bırakarak yazınız. Liste: ").split()]
                print(en_yakin_cift(sayi, cift_liste))

            elif cagirilacak_fonk == "3":
                print("Örnek: tekrar_eden_elemanlar([1, 2, 3, 2, 1, 5, 6, 5, 5, 5])")
                tekrar_liste = [int(i) for i in input("(Sayıları boşluk bırakarak yazınız. Liste: )").split()]
                print(tekrar_eden_elemanlar(tekrar_liste))
            
            elif cagirilacak_fonk == "4":
                print("Örnek: matris_carpimi\nA Matrisi\n1 2 3 \n4 5 6 \nB Matrisi\n7 8\n9 10\n11 12")
                print("Matrisi bitirdikten sonra . girin.\n")
                matrisA = []
                matrisB = []
                print("A Matrisi için satırları girin: ")
                while True:
                    satirA = input("")
                    if satirA == ".":
                        break
                    matrisA.append([int (i) for i in satirA.split()])
                print("B Matrisi için satırları girin: ")
                while True:
                    satirB = input("")
                    if satirB == ".":
                        break
                    matrisB.append([int (j) for j in satirB.split()])

                print(matris_carpimi(matrisA, matrisB))

            elif cagirilacak_fonk == "5":
                print("Örnek: C:/Users/Win10/Desktop/Masaüstü/Python/school/giris_metni.txt")
                dosya_adi = input("(Dosya uzantısını da giriniz.) Dosya Yolu: ")
                print(kelime_frekans(dosya_adi))

            elif cagirilacak_fonk == "6":
                print("Örnek: en_kucuk_deger([1, 4, 6, 91, 2, 5])")
                kucuk_liste = [int(i) for i in input("(Sayıları boşluk bırakarak yazınız. Liste: )").split()]
                print(en_kucuk_deger(kucuk_liste))

            elif cagirilacak_fonk == "7":
                print("Örnek: karekok(N=10000, x0=0.1, maxiter=15")
                karekoksayi = int(input("Karekökü alınacak sayıyı giriniz: "))
                ilktahmin = input("İlk tahmini giriniz: ")
                ilktahmin = float(ilktahmin)
                maxiter = input("Bir şey girmek istemiyorsanız N girin. Max Iter değeri giriniz: ").lower()
                if maxiter == "n":
                    print(karekok(karekoksayi, ilktahmin))
                else:
                    maxiter = int(maxiter)
                    print(karekok(karekoksayi, ilktahmin, maxiter=maxiter))


            elif cagirilacak_fonk == "8":
                print("Örnek: eb_ortak_bolen(18,64)")
                ilksayi = int(input("İlk sayı: "))
                ikincisayi = int(input("İkinci sayı: "))
                print(eb_ortak_bolen(ilksayi, ikincisayi))

            elif cagirilacak_fonk == "9":
                print("Örnek: asal_veya_degil(35)")
                asalsayi = int(input("Sayı giriniz: "))
                print(asal_veya_degil(asalsayi))

            elif cagirilacak_fonk == "10":
                print("Fibonacci hesabı")
                fib_n = int(input("Hesaplanacak olan fibonacci sayısı: "))
                print(hizlandirici(fib_n, 1, 1, 0))
                

            elif cagirilacak_fonk == "11":
                break

            else: # Kullanıcıdan beklenen değer dışında bir değer gelmesi durumunda hata gösterimi.
                print("Geçerli bir değer giriniz. ")

# Menü için renk alıyoruz. Kullanıcı geçersiz veya boş değer girerse mavi olacaktır.
menu_color = input("Menü rengi giriniz. \n(Varsayılan değer mavi olacaktır.) \n(Black, Blue ,Green, Aqua, Red, Purple, Yellow, White, Gray, Light Blue)\nRenk: ").lower()

menu = Menu(menu_color) # Menü objemizi oluşturduk.

menu.getMenu() # Menü objemizden getMenu() metodumuza ulaşıyoruz.  
