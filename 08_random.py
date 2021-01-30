import random

sayi1= random.random()
print(sayi1)

sayi2= random.randint(0,100)
print(sayi2)

sayi3= random.uniform(1.7,8.5)
print(sayi3)

liste=[5,12,8,6,"Eslem","Gizem",8.4, "Emin"]
deger= random.choice(liste)
print(deger)


# Kullanıcının itediği eleman sayısında bir diziyi 0-100 aralığında
# rastgele sayılarla doldurup bu sayıların ortalamasını yazdırınız.

eleman=int(input("Dizi kaç elemandan oluşsun?"))
dizi=[]

for i in range(eleman):
    dizi.append(random.randint(0,100))
print(dizi)

toplam=0
for x in (dizi):
    toplam +=x
print("Listedeki sayıların toplamı:", toplam)

ort= toplam/ eleman
print("Listedeki sayıların ortalaması:", ort)