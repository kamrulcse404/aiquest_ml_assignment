num1 =  int(input("Enter number 1: "))

cnt = 0

while num1 != 0:
    num1 = num1 // 10;  
    cnt += 1

print("the number of digit = {}".format(cnt))