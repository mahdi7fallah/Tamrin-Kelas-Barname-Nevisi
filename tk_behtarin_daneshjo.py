# دریافت نام و نمره تعدادی دانشجو
# نشان دادن دانشجویی که بالاترین نمره را دارد

#pylint:disable=C0103

tedad = int(input("Tedad DaneshjoyHa: "))

daneshjo_nomre = []          # Tedad Kole DaneshjoHa Ba Nomre
d_name = []                  # Name DaneshjoHa
d_nomre = []                 # Nomre DaneshjoHa
dict_d = {}                  # Dictionery

for i in range(tedad):
    d_name += [input("\nName Daneshjo {}: ".format(i + 1))]
    daneshjo_nomre += [d_name[i]]
    
    d_nomre += [input("Nomre {}: ".format(d_name[i]))]
    daneshjo_nomre += [d_nomre[i]]
    
    dict_d[d_name[i]] = d_nomre[i]
    
max_nomre = max(d_nomre)                       # Pehda Kardan Behtarin Nomre
index_max_nomre = d_nomre.index(max_nomre)     # Index Behtarin Nomre
behtarin_daneshjo = d_name[index_max_nomre]    # Behtarin Daneshjo

# print("\n", dict_d)
# print("\n", daneshjo_nomre)
# print("\nName  DaneshjoHa: ", d_name)
# print("Nomre DaneshjoHa: ", d_nomre)
print("\nBehtarin Nomre: ", max_nomre)
# print("Shamoreye Behtarin Nomre(Daneshjo): ", index_max_nomre + 1)
print("Behtarin Daneshjo: ", behtarin_daneshjo)
