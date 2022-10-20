"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

m = randint(0, 100)
array = [randint(0, 100) for i in range(2 * m + 1)]


def median(unsorted_list):
    a = unsorted_list
    try:
        if len(a) % 2 == 0:
            for j in range(len(a) // 2 - 1):
                a.pop(a.index(max(a)))
            q = a.pop(a.index(max(a)))
            w = a.pop(a.index(max(a)))
            return (q + w) / 2
        if len(a) % 2 != 0:
            for i in range(len(a) // 2):
                a.pop(a.index(max(a)))
            return max(a)
    except ValueError:
        return f'max() arg is an empty sequence'


print(f'Медиана списка array: {median(array)}')
print(timeit('median(array)', globals=globals(), number=1000))

"""
Время выполнения скрипта при длине списка 
10 элементов - 0.0004563000111375004
100 элементов - 0.0005400999798439443
1000 элементов - 0.002702300000237301
Улучшил скрипт - дописал возможность находить медиану в четном списке.
Но для подсчета времени лучше использовать отдельно скрипт для четных списков, отдельно для нечетных списков"""
