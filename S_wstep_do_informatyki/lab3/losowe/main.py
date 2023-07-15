from random import uniform
from random import randint

def los_int(a,b):
    x=a-b
    return x

a=int(input('podaj a: '))
b=int(input('podaj b: '))

for i in range(15):
    print(uniform(a,b))
    print(randint(a,b))