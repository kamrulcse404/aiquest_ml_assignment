sum = 0
while True:
    num = int(input("enter a number: "))
    if num < 0:
        break
    sum += num

print(f"sum = {sum}")