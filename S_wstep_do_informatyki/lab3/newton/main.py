from random import randint

def silnia(a):
    pom = 1
    for i in range(1,a+1):
        pom = pom * i
    return pom

def newton(a,b):
    pom = silnia(a)/(silnia(b)*silnia(a-b))
    return pom

def suma(a):
    if a==0: return 1
    else: return a+suma(a-1)+1

x = randint(0,10)
y = randint(0,10)
z=int(input('podaj z: '))
w=(silnia(x)-silnia(y)+silnia(z))/suma(x)
print(w)
