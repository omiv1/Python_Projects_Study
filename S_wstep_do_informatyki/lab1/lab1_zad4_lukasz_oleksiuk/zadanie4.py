from math import pow
k = 0
p = 0
lib = 0
lid = 0
while p == 0:
    k = int(input('Podaj "1" dle konwersji z systemy binarnego na dziesiętny\nPodaj "2" dle konwersji z ststemu dziesiętnego na binarny '))
    if k == 1 or k == 2:
        p = 1

if k == 1:
    l = int(input('Podaj liczbę binarną: '))
    licz = l
    liczbab = []
    while licz > 0:
        liczbab.append(licz % 10)
        licz = licz // 10
    for i in range(len(liczbab)):
        lib = lib + (liczbab[i] * pow(2, i))
    print(lib)
if k == 2:
    l = int(input('Podaj liczbę dziesiętną: '))
    licz = l
    liczbad = []
    while licz > 0:
        if (licz % 2) == 0:
            liczbad.append(0)
            licz = licz/2
        else:
            liczbad.append(1)
            licz = (licz-1)//2
    for i in range(len(liczbad)):
        lid = lid + (liczbad[i] * pow(10, i))
    print(lid)
