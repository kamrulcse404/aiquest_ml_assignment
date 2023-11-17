string = input('Enter a string: ')
ck = True

def my_func(string):
    my_dict = {}
    for i in string:
        if i in my_dict:
            global ck
            ck = False
            break
        else:
            my_dict[i] = 0

my_func(string)

if ck:
    print(f'{string} contains all unique characters')
else:
    print(f'{string} is not contain all unique characters')