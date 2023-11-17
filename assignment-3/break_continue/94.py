while True:
    password = input("enter password : ")

    if len(password) >= 8:
        continue
    
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    
    if not digit:
        continue

    upcase = False
    for up in password:
        if up.isupper():
            upcase = True

    if not upcase:
        continue

    locase = False
    for lo in password:
        if lo.islower():
            locase = True

    if not locase:
        continue

    print("Password accepted")
    break
