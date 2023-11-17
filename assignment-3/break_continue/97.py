while True:
    string = input("Enter string: ")
    string = string.lower()

    if len(string) < 3:
        continue

    l = len(string)
    i = 0
    j = l - 1
    ck = 1

    while i <= j:
        if string[i] != string[j]:
            ck = 0
            break
        i += 1
        j -= 1

    if ck == 1:
        print("{} is a Palindrome".format(string))
        break
    else:
        print("{} is not a Palindrome. Try again.".format(string))
