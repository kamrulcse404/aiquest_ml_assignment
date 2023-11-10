n =  int(input("Enter number : "))

f1 = 0
f2 = 1
if n <= 2:
    if n == 1:
        print(f1)
    elif n == 2:
        print(f1, f2)
else:
    print(f1)
    print(f2)
    for i in range(3, n+1):
        tmp = f1 + f2
        print(tmp)
        f1 = f2
        f2 = tmp