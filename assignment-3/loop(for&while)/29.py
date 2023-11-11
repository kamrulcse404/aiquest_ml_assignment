string = input('enter a string : ')

string = list(string)
# print(string)

i = 0
j =  len(string) - 1

# print(j)


while(i < j):
    tmp = string[i]

    string[i] = string[j]
    string[j] = tmp

    i = i + 1
    
    j = j -1


string = ''.join(string)
print(string)