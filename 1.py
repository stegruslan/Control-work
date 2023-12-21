"""
Сделайте функцию, которая создаст новый список из этого, заменив None на 0
"""

test_lst = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]


def func_none(test_lst: list) -> list:
    """
    Функция , которая создает новый список, заменяя 'None' на '0'
    :param test_lst:
    :return: list
    """
    new_lst = []
    for i in test_lst:
        new_lists = []
        for item in i:
            if item is None:
                new_lists.append(0)
            else:
                new_lists.append(item)
        new_lst.append(new_lists)
    return new_lst


print(func_none(test_lst))

