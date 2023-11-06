year =  int(input("Enter year : "))

if year % 400 == 0 or year % 4 == 0:
    print("{} is leap year".format(year))
elif year % 100 == 0:
    print("{} is not leap year".format(year))
else:
     print("{} is not leap year".format(year))