#Döngü Başlatma
#while (mantık cümlesi):
#        Yapılacak işlemler
#        Arttırma işlemleri

i=0
while (i<20):
    print("i'nin değeri:", i)
    i = i+2

defkullanici="eslemce"
defparola=12345

while True:
    kullanıcı=input("Kullanıcı adını giriniz:")
    parola= int(input("Parolanızı giriniz:"))

    if ((kullanıcı==defkullanici and parola ==defparola)):
        print(("Hoşgeldiniz", kullanıcı))
        break

    elif ((kullanıcı!=defkullanici and parola ==defparola)):
        print("Kullanıcı adını yanlış girdiniz")

    elif ((kullanıcı==defkullanici and parola !=defparola)):
        print("Şifrenizi mi unuttunuz?")
        print("Şifrenizi değiştirmek ister misiniz? (E/H)")
        cevap= input()
        if (cevap=="E"):
            yeniparola=input("Yeni Parola:")
            print("Lütfen Bekleyiniz")
            defparola=yeniparola
            print("Şifreniz Başarıyla Değiştirildi")

    else:
        print("Tekrar Deneyiniz")