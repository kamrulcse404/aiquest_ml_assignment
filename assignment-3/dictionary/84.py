my_dict = {}

string = input('Enter a string: ')

for i in string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)