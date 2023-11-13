import random

res = random.randrange(1, 101)
i = 1
print("Guess the number 1 to 100 ")
while True:
    num = int(input("{} try: ".format(i)))
    i = i + 1
    if num != res:
        continue
    else :      
        print("congratulations!! you guessed the number.")
        break
    