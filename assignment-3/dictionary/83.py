my_dict = {
    'joy': 30,
    'reza': 29,
    'hasan': 26,
    'masud': 32,
    'easha': 28
    }

my_dict = sorted(my_dict.items(), key=lambda x: x[1])

print(dict(my_dict))
