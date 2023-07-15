liczby = []
litery = []
ile = 3

for i in range(ile):
    print('podaj', chr(97+i), ':', end=' ')
    liczby.append(int(input()))
    litery.append(chr(97+i))

liczby.append('war')

for j in range(ile):
    for i in range(ile-1):
        if liczby[i] < liczby[i+1]:
            pom1 = liczby[i]
            liczby[i] = liczby[i+1]
            liczby[i+1] = pom1

            pom2 = litery[i]
            litery[i] = litery[i+1]
            litery[i+1] = pom2

pom = liczby[0]
k = 0

print('największe liczby:', end=' ')
while pom==liczby[k]:
    print(litery[k], end=' ')
    k = k+1


