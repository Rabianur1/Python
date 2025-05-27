#SORU 1:
list=[]
elemanlar=input("Liste için elemanları giriniz(Araya boşluk bırakarak): ").split()
list.extend(elemanlar)
tekrar={}
for eleman in list:
    if list.count(eleman)>1:
        tekrar[eleman] = list.count(eleman)
if tekrar:
      for eleman,ayni in tekrar.items():
        print(f"{eleman}: {ayni} kez")
else:
    print("Listede tekrar eden eleman yok.")




#SORU 2:
liste = list(map(int, input("Liste için elemanları giriniz(Araya boşluk bırakarak): ").split()))
if len(liste)>1:
    liste.remove(max(liste))  
    ikinci_buyuk=max(liste)
    print(f"Listedeki en büyük ikinci sayı: {ikinci_buyuk}")
else:
    print("Listede en büyük ikinci sayı yok.")




#SORU 2:
list=[]
elemanlar=input("Liste için elemanları giriniz(Araya boşluk bırakarak): ").split()
list.extend(elemanlar)
if len(list)>1:
    list.remove(max(list))  
    ikinci_buyuk=max(list)
    print(f"Listedeki en büyük ikinci sayı: {ikinci_buyuk}")
else:
    print("Listede en büyük ikinci sayı yok.")




#SORU 3:
liste = list(map(int, input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()))
kucukten_buyuge=sorted(liste)
print(f"Küçükten büyüğe sıralanmış liste: {kucukten_buyuge}")
kucukten_buyuge.reverse()
print(f"Büyükten küçüğe sıralanmış liste: {kucukten_buyuge}")




#SORU 3:
list=[]
elemanlar=input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()
list.extend(elemanlar)
kucukten_buyuge=sorted(list)
print(f"Küçükten büyüğe sıralanmış liste: {kucukten_buyuge}")
kucukten_buyuge.reverse()
print(f"Büyükten küçüğe sıralanmış liste: {kucukten_buyuge}")




#SORU 4:
liste = list(map(int, input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()))
yeni_liste=[eleman*2 for eleman in liste]
print(f"2 ile çarpılmış yeni liste: {yeni_liste}")




#SORU 4:
list=[]
elemanlar=input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()
list.extend(elemanlar)
yeni_liste=[int(eleman)*2 for eleman in list]
print(f"2 ile çarpılmış yeni liste: {yeni_liste}")




#SORU 5:
import random
liste = list(map(int, input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()))
random.shuffle(liste)
print(f"Karıştırılmış yeni liste: {liste}")




#SORU 5:
import random
list=[]
elemanlar=input("Liste için elemanları giriniz (Araya boşluk bırakarak): ").split()
list.extend(elemanlar)
random.shuffle(list)
print(f"Karıştırılmış yeni liste: {list}")
