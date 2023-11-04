num =  int(input("Enter number : "))

i = 1
res = 0

while i <= num :
    if i % 2 == 0 :
        res += i 
    i = i + 1

print("sum of even numbers 1 to {} is = {}" .format(num, res))