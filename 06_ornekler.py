#Bir metin iste. Sesli ve sessiz harflerini ayır.

metin=input("Lütfen bir metin giriniz:")
print("*"*20,"SESLİ HARFLER","*"*20 )
sesli="aeıioöuüAEIİOÖUÜ"
a=len(metin)
for i in range(1,a+1):
    b=metin[a-i]
    if b in sesli:
        print(b,end="\n")

print("*"*20,"SESSİZ HARFLER","*"*20 )
for i in range(1,a+1):
    b=metin[a-i]
    if b in sesli:
        print ("","")
    else:
        print(b)

###############
ad="Eslem"
soyad="Çataler"

if len(ad)>len(soyad):
    uzun=len(ad)
else:
    uzun=len(soyad)

for i in range(0,uzun):
    if len(ad)>i:
        print(ad[i],end=" ")
    else:
        print("*",end= " ")
    if len(soyad)>i:
        print(soyad[i],end=" ")
    else:
        print("*",end= " ")

