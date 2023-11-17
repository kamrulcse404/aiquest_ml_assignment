my_list = [[1, 2, 3], [1,4, 5, 6],[1, 7, 8, 9], 12]


my_dict = {}


for sub_list in my_list:
    if isinstance(sub_list, list):
        for i in sub_list:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] = my_dict[i] + 1
    else:
        if sub_list not in my_dict:
             my_dict[sub_list] = 1
        else:
            my_dict[sub_list] = my_dict[sub_list] + 1

print(my_list)
print(my_dict)