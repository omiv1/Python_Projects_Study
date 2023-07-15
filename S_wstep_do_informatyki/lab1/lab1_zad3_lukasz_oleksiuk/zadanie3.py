a = int(input('podaj a: '))
b = int(input('podaj b: '))
c = int(input('podaj c: '))

delta = (b*b)-(4*(a*c))

if delta > 0:
    x1 = (-b - delta) / (2 * a)
    x2 = (-b + delta) / (2 * a)
    print('x1 = ', x1, ', x2 = ', x2)
elif delta == 0:
    x = (-b)/(2*a)
    print('x = ', x)
else:
    print('funkcja nie posiada pierwiastków')
