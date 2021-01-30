faktöriyel=1

while True:
    sayi=int(input("Kaç fakötiyel girmek istiyorsunuz?"))
    if sayi<0:
        print("Negatif olamaz")
    else:
        for i in range(1,sayi+1):
            faktöriyel = faktöriyel*i
        print("Faktöriyeliniz:", faktöriyel)
        break