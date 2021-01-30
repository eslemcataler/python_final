#Selection Shorting

a=[5,2,18,90,-5,-1,7,68]

def secerek_siralama(Vektor):
    for i in range(len(Vektor)-1):
        enk=Vektor[i]
        enk_indis=i
        for j in range(i+1, len(Vektor)):
            if Vektor[j]<enk:
                enk=Vektor[j]
                enk_indis=j

        depo=Vektor[i]
        Vektor[i]=Vektor[enk_indis]
        Vektor[enk_indis]=depo

    print(Vektor)

secerek_siralama(a)

#Bubble Shorting

vekt=[5,3,1,10,-3,8]

def kabarcik_siralama(vektor):
    for i in range(len(vektor)-1):
        for j in reversed(range(i+1,len(vektor))):
            if vektor[j]<vektor[j-1]:
                depo=vektor[j-1]
                vektor[j-1]=vektor[j]
                vektor[j]=depo

    print(vektor)

kabarcik_siralama(vekt)