n = int(input("enter a number: "))

for i in range(n):
    star = ''
    for j in range(i+1):
        star = star + '*'
    
    print(star)