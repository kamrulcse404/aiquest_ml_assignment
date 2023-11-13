my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def dict_func(my_dict):
    return len(my_dict)


l = dict_func(my_dict)

print(f"lenth of this dictionary is = {l}")