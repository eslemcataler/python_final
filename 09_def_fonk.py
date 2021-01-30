def merhaba():
    print("Merhaba Dünya")


merhaba()

#silindirin hacmi
#pi*r*r*h

pi=3.14
def hacim(pi,r,h):
    return pi*r*r*h


print(hacim(pi,10,20))

#üçe böl
def uc_bol(sayi):
    return sayi/3

print(uc_bol(105))


# denklem kökü bulma
#axx + bx + c

def kok_bul(a,b,c):
    delta=(b*b - 4*a*c)
    if (delta<0):
        print("Reel kök yok")
        return

    x1 = (-b - delta ** 0.5) / 2 * a
    x2 = (-b + delta ** 0.5) / 2 * a

    return (x1,x2)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kok_bul(a,b,c)

print(sonuc)

