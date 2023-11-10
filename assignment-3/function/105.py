li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def list_sum(li):
    sum = 0
    for i in li :
        sum = sum + i

    print("sum of all elements from your list is = {}".format(sum))

list_sum(li)