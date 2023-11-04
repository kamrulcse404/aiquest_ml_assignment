import random

res = random.randrange(1, 11)
i = 1
print("Guess the number 1 to 10 ")
while True:
   
    if i <= 3 :
        num = int(input("{} try: ".format(i)))
        if num == res:
            print("congratulations!! you guessed the number.")
            break
    else : 
        print("you are loser")
        break
    i = i + 1
    


