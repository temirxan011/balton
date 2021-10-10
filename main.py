import Add_dict
import Iearn_dict

choice = int(input('1| Учить словарь\n2| Добавить словарь\nВЫБОР:'))

if choice == 1:
    Iearn_dict.learn_dict()
if choice == 2:
    Add_dict.add_dict()