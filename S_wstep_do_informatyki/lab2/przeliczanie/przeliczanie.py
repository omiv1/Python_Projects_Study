a = input('podaj wartość: ')
b = int(input('w jakim systemie jest zapisana liczba? '))
c = int(input('na jaki system ma zostać przeliczna liczba? '))

liczba = []
dl = len(a)
for i in range(dl):
    x = a[i]
    if x == '0': liczba.append(0)
    if x == '1': liczba.append(1)
    if x == '2': liczba.append(2)
    if x == '3': liczba.append(3)
    if x == '4': liczba.append(4)
    if x == '5': liczba.append(5)
    if x == '6': liczba.append(6)
    if x == '7': liczba.append(7)
    if x == '8': liczba.append(8)
    if x == '9': liczba.append(9)
    if x == 'a' or x == 'A': liczba.append(10)
    if x == 'b' or x == 'B': liczba.append(11)
    if x == 'c' or x == 'C': liczba.append(12)
    if x == 'd' or x == 'D': liczba.append(13)
    if x == 'e' or x == 'E': liczba.append(14)
    if x == 'f' or x == 'F': liczba.append(15)
x = 0
liczba.reverse()
for i in range(dl):
    x = x + (liczba[i] * pow(b,i))
liczba.clear()
while x > 0:
    pom = x-((x//c)*c)
    liczba.append(pom)
    x = x//c
liczba.reverse()
out = ''
for i in range(len(liczba)):
    x = liczba[i]
    if x == 0: out = out + '0'
    if x == 1: out = out + '1'
    if x == 2: out = out + '2'
    if x == 3: out = out + '3'
    if x == 4: out = out + '4'
    if x == 5: out = out + '5'
    if x == 6: out = out + '6'
    if x == 7: out = out + '7'
    if x == 8: out = out + '8'
    if x == 9: out = out + '9'
    if x == 10: out = out + 'A'
    if x == 11: out = out + 'B'
    if x == 12: out = out + 'C'
    if x == 13: out = out + 'D'
    if x == 14: out = out + 'E'
    if x == 15: out = out + 'F'
print(a,'(',b,') = ',out,'(',c,')')




