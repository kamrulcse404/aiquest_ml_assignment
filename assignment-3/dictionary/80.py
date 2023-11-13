my_dict = {
    'laptop': 10000,
    'phone': 12000,
    'ipad': 45000,
    'watch': 32000
    }

def dict_func(my_dict, price):
    ck = True
    for key, value in my_dict.items():
        if value == price:
            print(f"{key}")
            ck = False
            break
    if ck:
        print("item is not found with this price")



price = int(input('Enter price: '))

dict_func(my_dict, price)
