string = input("Enter number : ")

def is_palindrome(is_palindrome):
    l = len(string)
    i = 0
    j = l - 1
    ck = True
    while i <= j:
        if string[i] != string[j]:
            ck = False
            break
        i = i + 1
        j = j - 1

    if ck:
        print("True")
    if ck == False:
        print("False")

is_palindrome(string)