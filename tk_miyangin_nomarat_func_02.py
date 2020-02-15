
my_dict = {}

def ghaboli (td, tn):
    for i in range(td):
        nomre = 0
        name = input('Name Daneshjo {}: '.format(i + 1))
        
        for j in range(tn):
            nomre += int(input('Nomre {} {}: '.format(j + 1, name)))
        
        print('Miyanghin Nomarat {}: {}'.format(name, nomre / tn))
        print()
        my_dict[name] = nomre / tn
    
    miyangin_kol = sum(my_dict.values()) / td
    print('Miyangin Kol: ', miyangin_kol)
    
    print('==========================')
    
    for i in my_dict:
        if my_dict[i] >= miyangin_kol:
            print(i, my_dict[i], 'satisfy')
        else:
            print(i, my_dict[i], 'unsatisfy')
        


n = int(input('Tedad Daneshjo: '))
t = int(input('Tedad Nomre Har Daneshjo: '))

print('==========================')

ghaboli(n, t)

