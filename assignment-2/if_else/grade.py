
percentage = float(input("write the percentage: "))

if percentage >= 90 and percentage <= 100:
    print("your grade is A+")

elif percentage >= 80 and percentage < 90:
    print("your grade is A")

elif percentage >= 70 and percentage < 80:
    print("your grade is B")

elif percentage >= 60 and percentage < 70:
    print("your grade is C")

elif percentage >= 50 and percentage < 60:
   print("your grade is D")

elif percentage >= 0 and percentage < 50:
    print("your grade is F, you are fail")
else:
    print("you should write percentage between 0 to 100")

