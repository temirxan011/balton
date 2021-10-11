import os


def learn_dict():
    os.system('CLS')
    statistics_right = statistics_wrong = 0  # переменные для введения статистики
    # вывод всех словарей
    dict_list = os.listdir(path='./dict')
    print('\nСПИСОК ДОСТУПНЫХ СЛОВАРЕЙ')
    for i in dict_list:
        print('| ' + i, end=' ')

    # запись данных из файла в список
    name_dict = input('\nВведите название словаря: ')
    with open('./dict/' + name_dict + '.txt', 'r') as f:
        dict = f.read().split("|")

    # процесс обучения и проверки правильности перевода
    print('\n----------|' + name_dict + '|-----------')
    for i in range(0, (len(dict)//2) + 2, 2):
        print(dict[i])
        str_translite = input('Перевод: ')
        if str_translite == dict[i + 1]:
            print('ПРАВИЛЬНО' + '\n-----------------------------')
            statistics_right += 1
        else:
            print('ОШИБКА,' + ' ПРАВИЛЬНЫЙ ОТВЕТ: ' + dict[i+1] + '\n-----------------------------')
            statistics_wrong += 1
    print('--------|' + 'СТАТИСТИКА' + '|---------' + '\nПРАВИЛЬНО: ', statistics_right,  ' | НЕПРАВИЛЬНО: ', statistics_wrong)