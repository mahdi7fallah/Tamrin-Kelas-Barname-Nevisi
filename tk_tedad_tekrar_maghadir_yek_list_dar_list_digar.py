
# سوال صحیح: برنامه ای بنویسید که ۱۰ نام را به عنوان ورودی دریافت کرده و تعداد تکرار اسامی موجود یک لیست دیگر مثلا x را در بین نام های ورودی نمایش دهد.

list_x = ['ali', 'mmd', 'mahdi', 'reza', 'amir', 'omid', 'hossein', 'mahdi', 'mmd', 'taha', 'mahdi']
Name = []
n = int(input("Tedad NamHa: "))
dict_name_count = {}
print()

for i in range(n): # دریافت نام ها
    Name += [input("Name {}: ".format(i + 1))]
print()

for i in Name: # بررسی تعداد نام های Name در list_x
    print("Tedad {} Dar list_X: {}".format(i, list_x.count(i))) # نمایش تعداد نام های Name در list_x
    dict_name_count[i] = list_x.count(i) # افزودن نام و تعداد در دیکشنری
print()

print(dict_name_count, '\n\n')

print('list_x: ', list_x)
print('Name: ', Name)
