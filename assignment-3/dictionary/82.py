my_dict = {
    'laptop': 3,
    'phone': 4,
    'ipad': 6,
    'watch': 9
    }

key = input('enter the key name: ')

def my_fuc(my_dict, key):
    ck = True
    for i in my_dict:
        if i == key:
            my_dict.pop(key)
            print(f"updated dictionary = {my_dict}")
            ck = False
            break
    if ck:
        print(f"{key} key is not found")

my_fuc(my_dict, key)



