
# دریافت نام و نمرات تعدادی دانشجو
# گرفتن میانگین نمرات هر دانشجو
# گرفتن میانگین کل کلاس
# اگر میانگین نمرات دانشجویی از میانگین کل نمرات کلاس بیشتر یا مساوی بود satisfy و نمره را چاپ کن
# اگر میانگین نمرات دانشجویی از میانگین کل کلاس کمتر بود unsatisfy و نمره را چاپ کن


daneshjo_miyangin = {}                         # نام دانشجو و نمرات هر دانشجو
n = int(input('Tedad Daneshjoyan: '))          # تعداد دانشجویان
t = int(input('Tedad Nomaret Har Daneshjo: ')) # تعداد نمرات هر دانشجو

for i in range(n):
    nomre = 0
    daneshjo = input('\nName Daneshjo: ')      # دریافت نام
    
    for j in range(t):
        nomre += int(input('Nomre {}: '.format(daneshjo)) # دریافت نمره
        
    daneshjo_miyangin[daneshjo] = nomre / t               # ذخیره نام و میانگین نمره

miyangin_kol = sum(daneshjo_miyangin.values()) / n        # میانگین کل کلاس

print()
for i, j in daneshjo_miyangin:              # نمایش نام و نمره هر دانشجو
    print(i, ': '، j)
print('\nMiyangin Kol: ', miyangin_kol)     # نمایش میانگین کل کلاس

print()
for i, j in daneshjo_miyangin:
    if j >= miyangin_kol:
        print(i, j, 'satisfy') 
    else:
        print(i, j, 'unsatisfy')

