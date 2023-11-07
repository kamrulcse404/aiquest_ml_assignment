def palindrome(val) :
    l = len(val)
    i = 0
    j = l - 1
    ck = 1
    while i <= j:
        if val[i] != val[j]:
            ck = 0
            return False
        i = i + 1
        j = j - 1
    return True


val = input("Enter string : ")

ck = palindrome(val)

if ck == True:
    print("{} is Palindrome".format(val))
if ck == False:
    print("{} is not Palindrome".format(val))
