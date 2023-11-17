import math

a = int(input('enter a : '))
b = int(input('enter b : '))
c = int(input('enter c : '))

try:
    res1 = ((-b) + (math.sqrt(b**2 - 4*a*c))) / (2*a)
    res2 = ((-b) - (math.sqrt(b**2 - 4*a*c))) / (2*a)

    print(res1)
    print(res2)
except:
    print("the complex roots")