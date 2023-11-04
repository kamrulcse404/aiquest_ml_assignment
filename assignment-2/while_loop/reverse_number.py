num =  int(input("Enter number : "))
tmp = num
res = ''
while num > 0:
    mod = num % 10
    res = res + str(mod)
    num = num // 10

print('the number of {} reverse is = {}'.format(tmp, res))