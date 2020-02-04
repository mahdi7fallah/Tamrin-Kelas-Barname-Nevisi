a = ['Mohammad', 'Ali', 'Hasan', 'Hossein']
b = 'Mahdi'

print(list(enumerate(a)))
print(list(enumerate(a, 1)))
print()

for i, j in enumerate(a):
    print(i + 1, j)
print()

for i, j in enumerate(b):
    print("{}) {}".format(i + 1, j * 3))
print()

[print(i, ') ', i * j) for i, j in enumerate(b, 1)]
print()
