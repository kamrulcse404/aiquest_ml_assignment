num =  int(input("Enter number : "))

factorial = 1
i = 1

while i <= num :
    factorial *= i
    i = i + 1

print("factorial of {} is = {} ".format(num, factorial))