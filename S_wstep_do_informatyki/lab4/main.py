from math import sqrt
dane = open('trojki.txt','r')
wyniki = open('wyniki.txt','w')
wyniki_trojki = open('wyniki_trojki.txt','w')
trokaty = []
ile = 0
ile_r = 0
ile_o = 0
ile_p = 0
suma = 0
n = dane.readline()
n = int(n)
for i in range(n):
    trokaty.append(dane.readline())
    trokaty[i] = trokaty[i].split(" ")
    pom = trokaty[i]
    pom[3] = pom[3].replace("\n","")
    wiersz = pom[0]+pom[1]+pom[2]+pom[3]
    wiersz = int(wiersz)
    liczba_cyfr_w_wierszu = 0
    while(wiersz>0):
        liczba_cyfr_w_wierszu = liczba_cyfr_w_wierszu + (wiersz % 10)
        wiersz = wiersz//10
    wyniki_trojki.write(str(trokaty[i][0])+" "+str(liczba_cyfr_w_wierszu)+"\n")
    trokaty[i][0] = int(trokaty[i][0])
    trokaty[i][1] = int(trokaty[i][1])
    trokaty[i][2] = int(trokaty[i][2])
    trokaty[i][3] = int(trokaty[i][3])
    a = trokaty[i][1]
    b = trokaty[i][2]
    c = trokaty[i][3]
    m=max(a,b,c)
    if m < a+b+c-m:
        ile = ile + 1
wyniki.write("trojkat mozna zbudowac w "+str(ile)+" wierszach")
wyniki.write("\n")
for i in range(n):
    a = trokaty[i][1]
    b = trokaty[i][2]
    c = trokaty[i][3]
    if a >= b and a >= c:
        najw = a
        najm_1 = b
        najm_2 = c
    if b >= a and b >= c:
        najw = b
        najm_1 = a
        najm_2 = c
    if c >= a and c >= b:
        najw = c
        najm_1 = b
        najm_2 = a
    if najw < najm_1 + najm_2:
        wyniki.write(str(trokaty[i][0])+" ")
        wyniki.write(str(a)+" ")
        wyniki.write(str(b)+" ")
        wyniki.write(str(c)+" ")
        if pow(najw,2) > pow(najm_1,2) + pow(najm_2,2):
            wyniki.write("trojkat jest rozwartokatny")
            ile_r = ile_r + 1
        if pow(najw,2) < pow(najm_1,2) + pow(najm_2,2):
            wyniki.write("trojkat jest ostrokatny")
            ile_o = ile_o + 1
        if pow(najw,2) == pow(najm_1,2) + pow(najm_2,2):
            wyniki.write("trojkat jest prostokatny")
            ile_p = ile_p + 1
        p = (a + b + c) / 2
        pole = p * (p - a) * (p - b) * (p - c)
        pole = sqrt(pole)
        suma = suma + pole
        pole = round(pole,2)
        obw = a+b+c
        wyniki.write(", pole =")
        wyniki.write(" "+str(pole))
        wyniki.write(", obwod = "+str(obw))
        wyniki.write("\n")
suma = suma/ile
wyniki.write("liczba trojkatow rozwartokatnych = "+str(ile_r)+"\n")
wyniki.write("liczba trojkatow ostrokatnych = "+str(ile_o)+"\n")
wyniki.write("liczba trojkatow prostokatnych = "+str(ile_p)+"\n")
wyniki.write("srednia wielkosc trojkata wynisi "+str(round(suma,2)))
dane.close()
wyniki.close()
wyniki_trojki.close()
