num = int(input('num: '))
sum = 0

while(num):
    sum += num % 10
    num //= 10

print(sum)
