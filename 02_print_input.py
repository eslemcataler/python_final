###############
print("Eslem")
print('Gizem')
print("""Kübra""")

print('Eslem "Ben bu dersten geçmek istiyorum" dedi')
print("""Eslem "Ben bu dersten geçmek istiyorum" dedi""")
print('Eslem \"Ben bu dersten geçmek istiyorum\" dedi')

print("Eslem Ankara'ya gitmek istiyor")
print('Eslem Ankara\'ya gitmek istiyor')

####################

ad="Eslem"
soyad="Çataler"
yas=21

print("Merhaba", ad, soyad, "yaşın", yas)
print('Merhaba {} {} yaşın {}'.format(ad,soyad,yas))
print(f"Merhaba {ad} {soyad} yaşın {yas}")

##########################

print("Hocam nolur dersten geçirin", end=" ")
print("Lütfen")

print("Eslem", "Çataler", "Dersten", "Geçsin", sep="-")

print(*"Eslem", sep="*")

#######################

#\
print("Ahmet \"Ankara'ya gitmek istiyorum\" dedi")

#\n
print("birincivsatır\nikincivsatır\nüçüncü satır")

#\t
print("bir","iki","üç", sep="\t")

#\r
print("Merhaba\rDünya")

#\a
print("\a")

#\v
print("Düşey\v Sekme")

##################
ad= input("Adınızı giriniz:")
print(ad)
print(ad*5)
print(*"Çiçek")

yas=int(input("Yaşınız:"))
print("Yaşınız: {}".format(yas))
