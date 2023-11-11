# right-angled triangle

n = int(input("enter a number: "))

print('right-angled triangle')
print('   ')

for i in range(n):
    star = ''
    for j in range(i+1):
        star = star + '*'
    
    print(star)



print('   ')
# inverted right-angled triangle 
print('inverted right-angled triangle')
print('   ')

for i in range(n+1):
    star = ''
    for j in range(n - i):
        star = star + '*'
    print(star)





