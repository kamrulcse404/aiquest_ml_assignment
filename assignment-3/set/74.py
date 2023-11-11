a = {1, 2, 3, 4, 5, 9, 12}
b = {2, 3, 5, 6, 7, 8, 9}
c = {2, 3, 5, 8, 9, 13, 16}

intersection = a.intersection(b)

print("intersection of A and B = ", intersection)

union = b.union(c)

print("the union of B and C = ", union)

difference = c.difference(a)
print("difference between C and A = ", difference)
