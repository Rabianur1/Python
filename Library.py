from yardimci_modul import kutuphane_mesaji  #Yardımcı modül içindeki fonksiyonu içe aktarıyoruz

class Kitap:
    def __init__(self,ad,yazar):
        self.ad=ad
        self.yazar=yazar
        self.mevcut=True  #Başlangıçta kitap kütüphanede mevcuttur

    def odunc_ver(self):
        if self.mevcut:
            self.mevcut=False
            print(f"'{self.ad}' adlı kitap ödünç verildi.")
        else:
            print(f"'{self.ad}' adlı kitap şu an zaten ödünçte!")

    def iade_al(self):
        if not self.mevcut:
            self.mevcut = True
            print(f"'{self.ad}' adlı kitap iade alındı.")
        else:
            print(f"'{self.ad}' adlı kitap zaten kütüphanede bulunuyor.")

    def bilgi_yazdir(self):
        durum = "Mevcut" if self.mevcut else "Ödünçte"
        print(f"Kitap: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Durum: {durum}")

class Kutuphane:
    def __init__(self):
        self.kitaplar = []  #Kitap nesnelerini tutacak liste
        kutuphane_mesaji()  #Yardımcı modüldeki fonlsiyon çağrılır
        print("Kütüphane hizmete hazır!")

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"'{kitap.ad}'adlı kitap kütüphaneye eklendi.")
    
    def kitap_sayisi(self):
        toplam = len(self.kitaplar)
        print(f"\nToplam kitap sayısı: {toplam}")

#Kitapları ada göre alfabetik sıralar
    def kitaplari_sirala(self):
        sirali = sorted(self.kitaplar, key=lambda a: a.ad)
        print("\n----Alfabetik Kitap Listesi----")
        for kitap in sirali:
            kitap.bilgi_yazdir()

#Destructor Nesne silindiğinde çağrılır
    def __del__(self):
        print("Kütüphane sistemi kapatılıyor!")

if __name__ == "__main__":
    kutuphane=Kutuphane()

    kitap1=Kitap("Harry Potter ve Felsefe Taşı", "J.K. Rowling")
    kitap2=Kitap("Kürk Mantolu Madonna", "Sabahattin Ali")
    kitap3=Kitap("Küçük Prens", "Antoine de Saint-Exupéry")

    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)
    kutuphane.kitap_ekle(kitap3)
    kutuphane.kitap_sayisi()
    kutuphane.kitaplari_sirala()
    kitap1.odunc_ver()
    kitap1.iade_al()
    del kutuphane