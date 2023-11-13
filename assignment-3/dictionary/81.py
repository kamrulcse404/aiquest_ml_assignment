my_dict1 = {
    'laptop': 10000,
    'phone': 12000,
    'ipad': 45000,
    'watch': 32000
    }


my_dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

merge_dict =  {**my_dict1, **my_dict1}

print(merge_dict)