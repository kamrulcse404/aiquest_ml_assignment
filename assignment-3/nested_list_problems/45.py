my_list = [[1, 2, 3], [4, 5, 6],[7, 8, 9], 12]

new_list = []

for sub_list in my_list:
    if isinstance(sub_list, list):
        for i in sub_list:
            new_list.append(i)
    else:
        new_list.append(sub_list)

print(my_list)
print(new_list)