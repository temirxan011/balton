from googletrans import Translator


def add_dict():
    name_dict = input('Название словаря: ')
    word_count = int(input('Количество слова в словаре: '))
    # создание и заполнение файла
    with open('./dict/' + name_dict + '.txt', 'a') as f:
        translator = Translator()
        for i in range(word_count):
            proposal_text = input('Введите предложение: ')
            f.write(proposal_text + '/' + translator.translate(proposal_text).text + '\n')

    # вывод содержимого файла
    with open('./dict/' + name_dict + '.txt') as f:
        print('\n' + f.read())