def RNWD_euklidesowe_v2(m,n):
    d = m
    k = n
    s1 = 0
    s2 = 1
    while k:
        q = d // k
        d, k = k, d-q*k
        s1, s2 = s2, s1 - (q * s2)


    return s1

def odwrotna(m,n):
    x = RNWD_euklidesowe_v2(m, n)
    if x < 0:
        return m + x
    if n*x%m != 1:
        print("Nie ma rozwiązań m i n nie są względnie pierwsze !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return ""
    return x

def chinskaMetoda3():
    a1 = int(input("Podja pierwsze a: "))
    n1 = int(input("Podja pierwszy modulnik: "))
    a2 = int(input("Podja drugie a: "))
    n2 = int(input("Podja drugi modulnik: "))
    a3 = int(input("Podja trzecie a: "))
    n3 = int(input("Podja trzeci modulnik: "))

    aN1 = n2*n3
    aN2 = n1*n3
    aN3 = n1*n2

    aM1 = odwrotna(n1, aN1)
    aM2 = odwrotna(n2, aN2)
    aM3 = odwrotna(n3, aN3)

    wynik = (a1*aN1 * aM1 + a2*aN2 * aM2 + a3*aN3 * aM3)%(n1*n2*n3)

    return f'{str(wynik)} + {str(n1*n2*n3)}l'

def chinskaMetoda4():
    a1 = int(input("Podja pierwsze a: "))
    n1 = int(input("Podja pierwszy modulnik: "))
    a2 = int(input("Podja drugie a: "))
    n2 = int(input("Podja drugi modulnik: "))
    a3 = int(input("Podja trzecie a: "))
    n3 = int(input("Podja trzeci modulnik: "))
    a4 = int(input("Podja trzecie a: "))
    n4 = int(input("Podja trzeci modulnik: "))

    aN1 = n2*n3*n4
    aN2 = n1*n3*n4
    aN3 = n1*n2*n4
    aN4 = n1*n2*n3

    aM1 = odwrotna(n1, aN1)
    aM2 = odwrotna(n2, aN2)
    aM3 = odwrotna(n3, aN3)
    aM4 = odwrotna(n4, aN4)

    wynik = (a1*aN1 * aM1 + a2*aN2 * aM2 + a3*aN3 * aM3 + a4*aN4 * aM4)%(n1*n2*n3*n4)

    return f'{str(wynik)} + {str(n1*n2*n3*n4)}l'



def dwieKongruencje():
    a1 = int(input("Podja pierwsze a: "))
    n1 = int(input("Podja pierwszy modulnik: "))
    a2 = int(input("Podja drugie a: "))
    n2 = int(input("Podja drugi modulnik: "))


    a1Ram = a2-a1
    if a1Ram<0:
        a1Ram = n2 + a1Ram

    odw = odwrotna(n2, n1)

    a2Ram = a1Ram*odw %n2

    wynik = n1*a2Ram+a1
    zmienna = str(n2*n1)+" l"

    return str(wynik) +" + "+ zmienna

rownan = int(input("Ile masz rownań (2, 3 lub 4):"))

print("x = a (mod n)")
if rownan == 1:
    a = int(input("Modulnik:"))
    b = int(input("odwracalna:"))
    print(odwrotna(a, b))
elif rownan == 2:
    print(dwieKongruencje())
elif rownan == 3:
    print(chinskaMetoda3())
elif rownan == 4:
    print(chinskaMetoda4())
else:
    print("Podaj tylko liczbę od 2 do 4")