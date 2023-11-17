num = int(input('enter a number: '))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 7, 3, 5, 5, 5, 5]
cnt = 0
ck = True
for i in li:
    if num in li:
        if i == num:
            cnt = cnt + 1
    else:
        ck = False
        print(f"{num} is not exist in this given list")
        break
if ck:
    print(f"{num} occurs {cnt} times in the list")
