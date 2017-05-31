import math


def f_area(a, b, c):
    sol = 0
    s = (a + b + c)/2
    r = s*(s - a)*(s - b)*(s - c)
    if  r > 0:
        sol = math.sqrt(r)
    return sol

a, b = str(input()).split(" ")
a = int(a)
b = int(b)
while(a != 0 and b != 0):
    c = 1
    area = f_area(a, b, c)
    max = 0
    while (max == 0 or area > max):
        c += 1
        max = area
        area = f_area(a, b, c)
    print(round(area,1))
    a, b = str(input()).split(" ")
    a = int(a)
    b = int(b)
