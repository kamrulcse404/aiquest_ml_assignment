num = int(input("enter set elements : "))

my_set = {2, 3, 5, 6, 7, 8, 9, 4}
ck = False

for n in my_set:
    if n == num:
        ck = True
        break

if ck :
    print('Found')
else:
    print('Not Found')