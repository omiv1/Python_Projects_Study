a = int(input('podaj a: '))
b = int(input('podaj b: '))

i=0
d = []
s = []
t = []
d.append(a)
d.append(b)
n= 2
s.append(1)
s.append(0)
t.append(0)
t.append(1)
while d[n-1]>0:
    q=d[n-2]//d[n-1]
    pom = d[n - 2] - (q * d[n-1])
    d.append(pom)
    pom = t[n - 2] - (q * t[n - 1])
    t.append(pom)
    pom = s[n - 2] - (q * s[n - 1])
    s.append(pom)
    n=n+1
    print(d[n-1],' ',q,' ',s[n-1],' ',t[n-1])