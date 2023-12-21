"""
Напишите генератор, который принимает 2 параметра
(Пусть это будет образно генератор который делит продукцию максимально поровну на склады)
1 - количество возвращаемых значений (складов)
2 - количество продукции (продукции)
Например 100 продукции на 5
-> 20
-> 20
-> 20
-> 20
-> 20
Или например
97 продукции на 5
-> 19
-> 19
-> 19
-> 20
-> 20
Порядок не важен, можно (20, 20, 19, 19, 19)
Или 2 на 3
-> 1
-> 1
-> 0
Чтобы проверить работу можно использовать функцию ниже

"""


def test(*args):
    for _ in range(5):
        yield 1


def solution(storages, count):
    """
    Функция для которая поровну делит колличетво продукции 'count' , на склады 'storages'
    :param storages:
    :param count:
    :return: генератор 'yield'
    """
    for rest_storages in range(storages, 0, -1):
        c = count // rest_storages
        count -= c
        yield c


def check(func, a, b):
    print(list(func(a, b)))



check(solution, 7, 10)
