string = input('Enter a string: ')

string = string.lower()
cnt = 0

for i in string:
    if i != 'a' and i !=  'e' and i !=  'i' and i !=  'o' and i !=  'u':
        continue
    cnt = cnt + 1

print(f"Vowel in your string = {cnt}")