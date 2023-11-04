num1 =  int(input("Enter number 1: "))
num2 =  int(input("Enter number 2: "))
num3 =  int(input("Enter number 3: "))

if num1 >= num2 and num1 >= num3 :
    print("max number is number 1 = ", num1)
elif num2 >= num1 and num2 >= num3 :
    print("max number is number 2 = ", num2)
else:
    print("max number is number 3 = ", num3)