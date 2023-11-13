num = int(input("enter a number: "))
ck = True

for i in range(2, num):
    if num % i == 0:
        ck = False
        break

if ck:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")