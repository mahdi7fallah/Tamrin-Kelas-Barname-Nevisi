
num_start = int(input('Start Number: '))
num_end = int(input('End  Number :'))

list_number = [i for i in range(num_start, num_end + 1)]
num_aval = []

for i in list_number:
    adad_aval = True
    for j in range(2, i // 2):
        if i % j == 0:
            adad_aval = False
    if adad_aval == True:
        num_aval += [i]

print('\n', num_aval)
