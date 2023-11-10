year =  int(input("Enter year : "))

def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0:
        print("True")
    elif year % 100 == 0:
        print("False")
    else:
        print("False")

is_leap_year(year)