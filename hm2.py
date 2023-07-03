"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента.
(речь идет про **kwargs)
"""


def process_kwargs(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result


kwargs_dict = process_kwargs(car='01', age='5year', state='repaired')
print(kwargs_dict)
