num = int(input('Enter number: '))

def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num -1) + Fibonacci(num - 2)
    
res = Fibonacci(num)

print(f"{num} fibonacci number is {res}")
