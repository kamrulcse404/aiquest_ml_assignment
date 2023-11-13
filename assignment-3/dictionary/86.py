my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

key = input('Enter your key: ')

def my_func(my_dict, key):
    if key in my_dict:
        print('Key Found')
    else:
        print("Key Not Found")


my_func(my_dict, key)