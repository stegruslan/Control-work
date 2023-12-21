"""
Напишите скрипт, который прочитает файл 2.txt
И создаст новый файл 2_raint.txt
И точно так же запишет тот же текст, заменив все слова дождь на ДОЖДЬ
(большими буквами)
Учитывая окончания, например  дожде -> ДОЖДЕ
"""


'''Открываем файл 2.txt в режиме чтения,разбиваем
на отдельные слова и записываем новый список в переменную text'''

with open("2.txt", "r", encoding='utf-8') as f:
    text = [
        line.split()
        for line in f.readlines()
    ]


def rain():
    """
    Функция, меняющая окончания слов с корнем 'дожд'
    :return:
    """

    new_text = '\n'.join([
        ' '.join([
            word.upper() if 'дожд' in word.lower() else word
            for word in line
        ])
        for line in text
    ]) + '\n'

    with open("2_rain.txt", "w", encoding='utf-8') as f:
        f.write(new_text)


rain()
