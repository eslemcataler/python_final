sayi1=input("Sayı 1:")
sayi2=input("Sayı 2:")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)

except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")

except ValueError:
    print("Lütfen 10'luk tabanlı bir sayı giriniz.")
