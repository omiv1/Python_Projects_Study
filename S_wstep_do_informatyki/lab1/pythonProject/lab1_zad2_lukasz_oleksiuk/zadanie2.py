from math import sqrt

a = int(input('podaj a:'))
b = int(input('podaj b:'))
c = int(input('podaj c:'))

trojkat = [a, b, c]
trojkat.sort(reverse=True)

if trojkat[0] < trojkat[1]+trojkat[2]:
    print('można zbudować trójkąt')
    p = (a+b+c)/2
    pole = sqrt(p*(p-a)*(p-b)*(p-c))
    print('pole wynosi ', pole.__round__(3))
    if(trojkat[1]*trojkat[1])+(trojkat[2]*trojkat[2]) < (trojkat[0]*trojkat[0]):
        print('trójkąt jest rozwartokątny')
    elif(trojkat[1]*trojkat[1])+(trojkat[2]*trojkat[2]) == (trojkat[0]*trojkat[0]):
        print('trójkąt jest prostokątny')
    else:
        print('trójkąt jest ostrokątny')
else:
    print('nie można zbydować trójkąta')
