a =  int(input("Enter number 1: "))
b =  int(input("Enter number 2: "))
c =  int(input("Enter number 3: "))

if a == b and a == c :
    print("equilateral triangle")
elif a == b or b == c or c == a:
    print("isosceles triangle")
else :
    print("scalene triangle")