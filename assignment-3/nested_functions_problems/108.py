num1 = int(input('enter num1 : '))
num2 = int(input('enter num2 : '))
num3 = int(input('enter num3 : '))

op = input('what you want to do: ')
op = op.lower()



def add(num1, num2, num3):
    return num1 + num2 + num3

def subtract(num1, num2, num3):
    return num1 - num2 - num3
    
def multiply(num1, num2, num3):
    return num1 * num2 * num3
    
def divide(num1, num2, num3):
    return num1 / num2 / num3


def math_operations(num1, num2, num3, op):
    if op == 'add':
        return add(num1, num2, num3)
    
    elif op == 'subtract':
        return subtract(num1, num2, num3)
    
    elif op == 'multiply':
        return multiply(num1, num2, num3)
    
    elif op == 'divide':
        return multiply(num1, num2, num3)
    
res = math_operations(num1, num2, num3, op)

print(res)
