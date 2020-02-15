
# دریافت یک عدد از کاربر و نمایش فاکتوریل با استفاده از تابع

# Factorial n ===> 1 * 2 * 3 * ... * n



def factorial(number):
    f = 1
    for i in range(1, number + 1):
        f *= i
    print(f)

factorial(int(input("Number: ")))
