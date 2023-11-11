li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max_val = li[0]
min_val = li[0]

l = len(li)

sum = 0

for i in li:
    sum = sum + i
    if i > max_val:
        max_val = i
    if min_val > i :
        min_val = i


print("sum = {}".format(sum))
print("max value = {}".format(max_val))
print("min value = {}".format(min_val))
print("average value = {}".format(sum / l))

