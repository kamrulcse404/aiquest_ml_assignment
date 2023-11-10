num =  int(input("Enter number : "))

res = 0
for i in range(1, num+1) :
    res = res + i

print("sum of even numbers 1 to {} is = {}" .format(num, res))