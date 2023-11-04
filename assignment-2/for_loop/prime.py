num =  int(input("Enter number : "))
ck = 1

for i in range(2, num):
    if num % i == 0:
        ck = 0
        break

if ck == 0:
    print("{} is not a prime number".format(num))
elif ck == 1:
    print("{} is a prime number".format(num))