hour = int(input("Enter hour: "))

if hour >= 6 and hour < 12:
    print('Good Morning')
elif hour >= 12 and hour < 18:
    print('Good Afternoon')
elif hour >= 18 and hour < 24:
    print('Good Evening')
elif hour >= 0 and hour < 6:
    print('Good Night')