my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

def dict_func(my_dict):

    for key, value in my_dict.items():
        print(f"{key} => {value}")


dict_func(my_dict)