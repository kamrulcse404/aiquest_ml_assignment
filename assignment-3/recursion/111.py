num = int(input('Enter number: '))

def factorial(num):
    if num ==1:
        return 1
    else:
        return num * fact(num - 1)
    
res = factorial(num)

print(f"Factorial of {num} is {res}")