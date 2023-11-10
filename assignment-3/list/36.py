li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_val = li[0]
min_val = li[0]
for i in li :
    if max_val < i :
        max_val = i


for i in li :
    if min_val > i :
        min_val = i


print("max value is = {}".format(max_val))
print("min value is = {}".format(min_val))