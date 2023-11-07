num =  int(input("Enter number : "))

if num >= 0 and  num <= 50 :
    print("{} is in range 0-50".format(num))
elif num >= 51 and  num <= 100 :
    print("{} is in range 51-100".format(num))
elif num >= 101 and  num <= 150 :
    print("{} is in range 101-150".format(num))
else :
    print("{} is above 150".format(num))