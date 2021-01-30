# 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21

sinir= int(input("Kaç adet Fibonacci sayısı girmek istiyorsunuz?"))

sayi1=0
sayi2=1

print(sayi1)
print(sayi2)

for i in range(sinir-2):
    sayi3= sayi1+ sayi2
    print(sayi3)

    sayi1=sayi2
    sayi2= sayi3