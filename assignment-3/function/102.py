num =  int(input("Enter number : "))



def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

res = factorial(num)
print("factorial of {} is = {} ".format(num, res))