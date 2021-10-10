import os


def learn_dict():
    # вывод всех словарей
    dict_list = os.listdir(path='./dict')
    for i in dict_list:
        print(i, end=' | ')

    # запись данных из файла в список
    name_dict = input('\nВведите название словаря: ')
    with open('./dict/' + name_dict + '.txt', 'r') as f:
        dict = f.read().split("\n")

    # процесс обучения и проверки правильности перевода
    for i in range(0, (len(dict)//2) + 2, 2):
        print(dict[i])
        str_translite = input('Перевод: ')
        if str_translite == dict[i + 1]:
            print('OK')
        else:
            print('ERROR')