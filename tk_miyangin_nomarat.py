# دریافت نام و نمرات تعدادی دانشجو
# گرفتن میانگین نمرات هر دانشجو
# گرفتن میانگین کل کلاس
# اگر میانگین نمرات دانشجویی از میانگین کل نمرات کلاس بیشتر یا مساوی بود satisfy و نمره را چاپ کن
# اگر میانگین نمرات دانشجویی از میانگین کل کلاس کمتر بود unsatisfy و نمره را چاپ کن


daneshjo_miyangin = {}  # نام دانشجو و میانگین نمرات هر دانشجو
daneshjo_nomre = {}  # نام دانشجو و نمره
n = int(input('Tedad Daneshjoyan: '))  # تعداد دانشجویان
t = int(input('Tedad Nomaret Har Daneshjo: '))  # تعداد نمرات هر دانشجو

for i in range(n):
    majmo_nomre = 0
    no = []
    daneshjo = input('\nName Daneshjo {}: '.format(i + 1))  # دریافت نام

    for j in range(t):
        x = int(input('Nomre {} {}: '.format(j + 1, daneshjo)))  # دریافت نمره
        majmo_nomre += x
        no += [x]
    daneshjo_nomre[daneshjo] = no  # ذخیره نام و نمره
    daneshjo_miyangin[daneshjo] = majmo_nomre / t  # ذخیره نام و میانگین نمره

miyangin_kol = sum(daneshjo_miyangin.values()) / n  # میانگین کل کلاس

print('\nMiyangin Kol: ', miyangin_kol)  # نمایش میانگین کل کلاس

print()
for i in daneshjo_miyangin:
    if daneshjo_miyangin[i] >= miyangin_kol:
        print(i, daneshjo_miyangin[i], 'satisfy')
    else:
        print(i, daneshjo_miyangin[i], 'unsatisfy')

