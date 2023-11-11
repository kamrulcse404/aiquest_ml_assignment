student_value = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

def add_std(student_value, name, val):
    if name in student_value:
        student_value[name] = val
    else:
        student_value[name] = val

add_std(student_value, 'kamrul', 98)

print(student_value)