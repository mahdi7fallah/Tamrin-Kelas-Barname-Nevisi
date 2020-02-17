
contacts = {}
option_list = '''
1. Show Contacts
2. Add Contact
3. Edit Contact
4. Delete Contact
5. Search Contact
6. Exit
'''


'''============================================================================'''
def show_contacts():
    print('\n', "Contact List Menu".center(25,'*'))

    for i,j in contacts.items():
        print("{}: {}".format(i,j))

    print('=' * 25, '\n')

'''============================================================================'''

def add_contact():
    print('\n', "Add Contact Menu".center(25,'*'))

    c_name = input("Contact Name: ")
    c_number = input("Contact Number:")
    if not c_name == '' or c_number == '':
        contacts[c_name] = c_number

    print('=' * 25, '\n')

'''============================================================================'''

def edit_contact():
    print('\n', "Edit Contact Menu".center(25,'*'))

    while(True):
        c_o_name = input("Contact Name: ")
        if not c_o_name in contacts.keys():
            print("Name Not Found In Contact List!")
            break
        else:
            edit_option = input("1. Edit Name\n2. Edit Number\n3. Back\nPlease Enter Option Number:")
            if edit_option == '1':
                c_n_name = input("New Name For {}: ".format(c_o_name))
                contacts[c_n_name] = contacts[c_o_name]
                del contacts[c_o_name]
            elif edit_option == '2':
                c_n_number = input("New Number For {}:".format(c_o_name))
                contacts[c_o_name] = c_n_number
            elif edit_option == '3':
                break
            else:
                edit_option = input("Please Enter Option Number:")
            break

    print('=' * 25, '\n')

'''============================================================================'''

def delete_contact():
    print('\n', "Delete Contact Menu".center(25,'*'))

    c_name = input("Contact Name For Delete: ")
    if c_name in contacts.keys():
        del contacts[c_name]
        print("{} Deleted".format(c_name))
    else:
        print("Contact Name Not Found!")

    print('=' * 25, '\n')

'''============================================================================'''

def search_contact():
    print('\n', "Search Contact Menu".center(25,'*'))

    while(True):
        search_option = input("1. Search By Name\n2. Search By Number\n3. Back\nPlease Enter Option Number:")
        if search_option == '1':
            s_name = input("Enter Name For Search: ")
            if s_name in contacts.keys():
                print('=' * 25, '\n')
                print("{}: {}".format(s_name,contacts[s_name]))
                print('=' * 25, '\n')
            else:
                print("Name Not Found !")
        elif search_option == '2':
            s_number = input("Enter Number For Search: ")
            if s_number in contacts.values():
                for i, j in contacts.items():
                    if j == s_number:
                        print('=' * 25, '\n')
                        print('{}: {}'.format(i, j))
                        print('=' * 25, '\n')
            else:
                print("Name Not Found !")
        elif search_option == '3':
            break
    
    print('=' * 25, '\n')
'''============================================================================'''


while(True):
    n = input("{}Please Select Option Number: ".format(option_list))
    if   (n == '1') or (n == 'Show'):   show_contacts()
    elif (n == '2') or (n == 'Add'):    add_contact()
    elif (n == '3') or (n == 'Edit'):   edit_contact()
    elif (n == '4') or (n == 'Delete'): delete_contact()
    elif (n == '5') or (n == 'Delete'): search_contact()
    elif (n == '6') or (n == 'Exit'):   break
    else: pass

print("GoodBye !!!")
