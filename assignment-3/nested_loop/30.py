n = int(input("enter a number: "))

for i in range(1,n+1):
    star = ''
    for j in range(1,11):
        print("{} * {} = {}".format(i, j, i * j))