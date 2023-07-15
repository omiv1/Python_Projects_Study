def rek_1(a):
    if a == 1: return 2
    if a == 2: return 3
    if a > 2: return (2*rek_1(a-2)+rek_1(a-1))

def rek_2(a):
    if a == 1: return 1
    if a > 1: return ((2*rek_2(a-1))+1.5)

def rek_fib(a):
    if a == 0: return 1
    if a == 1: return 1
    if a > 1: return rek_fib(a-1)+rek_fib(a-2)

def rek_fib_minus(a):
    if a == 0: return -1
    if a == 1: return 1
    if a > 1 or a < 0:
        if a //2: return -1*((rek_fib(a-1)+rek_fib(a-2)))
        else: return (rek_fib(a-1)+rek_fib(a-2))

def rek_silnia(a):
    if a == 0: return 1
    if a > 0: return rek_silnia(a-1)*a

def silnia(a):
    pom = 1
    for i in range(1,a+2):
        pom = i * pom
    return pom

def zad2_c(a):
    if a == 0: return 1
    else: return 2*zad2_c(a-1)+1

a = int(input('podaj a: '))
for i in range(a):
    print(zad2_c(i))