
percentage = float(input("enter the percentage: "))

if percentage >= 90:
    print("your grade is A+")

elif percentage >= 80 and percentage <= 89:
    print("your grade is A")

elif percentage >= 70 and percentage <= 79:
    print("your grade is B")

elif percentage >= 60 and percentage <= 69:
    print("your grade is C")

elif percentage < 60:
   print("You are Fail")
else:
    print("you should write percentage between 0 to 100")