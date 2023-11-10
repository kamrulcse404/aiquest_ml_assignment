li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

j = len(li) - 1
i = 0

while i < j:
    tmp = li[i]
    li[i] = li[j]
    li[j] = tmp

    i= i + 1
    j = j - 1

print(li)