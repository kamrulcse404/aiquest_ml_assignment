# a = {2, 3, 4, 7, 6}
# b = {2, 3, 5, 6, 7, 8, 9, 4}

a = {1, 2, 3, 4, 5}
b = {1, 2, 3}

super_set = a.issuperset(b)

if super_set :
    print("a is a superset of b")
else:
    print("a is not a superset of b")