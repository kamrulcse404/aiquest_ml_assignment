li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 7, 3, 5, 5, 5, 5]
new_list = []

for i in li:
    if i not in new_list:
        new_list.append(i)

print(li)
print(new_list)