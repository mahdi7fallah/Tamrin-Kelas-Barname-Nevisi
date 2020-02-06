
num = 0
max1 = 0
max2 = 0
max3 = 0

tedad = int(input('tedad: '))
print()

for i in range(tedad):
    num = int(input('num {}: '.format(i + 1)))
    
    if num > max3: max3 = num
    if max3 > max2: max2, max3 = max3, max2
    if max2 > max1: max1, max2 = max2, max1

print('\n', max1)
print(max2)
print(max3)
