num1 =  int(input("Enter number 1 : "))
num2 =  int(input("Enter number 2 : "))

def gcd(num1, num2):

    if num1 > num2: 
        temp = num1
        num1 = num2
        num2 = temp

    while num2 % num1 != 0:
        mod = num2 % num1
        num2 = num1
        num1 = mod

    print("GCD is ", num1)

gcd(num1, num2)