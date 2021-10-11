import Add_dict
import Iearn_dict

while 1 == 1:
    choice = int(input('\n1| Учить словарь\n2| Добавить словарь\n3| ВЫЙТИ\nВЫБОР: '))
    if choice == 1:
        Iearn_dict.learn_dict()
    if choice == 2:
        Add_dict.add_dict()
    else:
        break