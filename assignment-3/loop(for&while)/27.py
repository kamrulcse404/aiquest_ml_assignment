num =  int(input("Enter number : "))
ck = 1
i = 2
while i < num :
    if num % i == 0:
        ck = 0
        break
    i = i + 1

if ck == 0:
    print("{} is not a prime number".format(num))
elif ck == 1:
    print("{} is a prime number".format(num))