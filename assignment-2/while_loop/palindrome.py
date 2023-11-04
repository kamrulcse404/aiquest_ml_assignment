string = input("Enter number : ")

l = len(string)
i = 0
j = l - 1
ck = 1
while i <= j:
    if string[i] != string[j]:
        ck = 0
        break
    i = i + 1
    j = j - 1

if ck == 1:
    print("{} is Palindrome".format(string))
if ck == 0:
    print("{} is not Palindrome".format(string))