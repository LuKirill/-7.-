"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit

m = randint(0, 100)
array = [randint(0, 100) for i in range(2 * m + 1)]


def pyramid(some_array):
    def heapsort(arr):
        n = len(arr)
        for i in range(n // 2, -1, -1):
            heapshift(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapshift(arr, i, 0)
        return arr

    def heapshift(arr, n, i):
        lagest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            lagest = left
        if right < n and arr[lagest] < arr[right]:
            lagest = right
        if lagest != i:
            arr[i], arr[lagest] = arr[lagest], arr[i]
            heapshift(arr, n, lagest)
    return heapsort(some_array)


def median(sorted_list):
    n = len(sorted_list)
    i = n // 2
    if n % 2:
        return sorted_list[i]
    return sum(sorted_list[i - 1:i + 1]) / 2


print(f'Неотсортированный случайный список: {array}')
p = pyramid(array)
print(f'Отсортированный список сортировкой КУЧА: {p}')
print(f'Медиана: {median(p)}')
print(f'Индекс медианы: {m}')
print(timeit('pyramid(array)', globals=globals(), number=1000))
print(timeit('median(array)', globals=globals(), number=1000))

"""
Для сортировки списка 2m + 1 я выбрал способ "КУЧА", тк этот способ имеет стабильную сложность О(n*logn), 
которая не изменяется от величины начального списка. Метод Гномья проще в написании, но имеет сложность O(n**2)
Метод Шелла (модифицированная сортировка вставками) в наилучшем случае имеет сложность O(n*logn) в худшем O(n**2).

Для удобства объединил вспомогательную функцию heapshift и основную heapsort в функцию pyramid.

Медиану ищем через функцию median, где рассматриваем 2 случая: 1й - если список четный, 2й - если список нечетный.

Расчет времени выполнения скрипта реализован при помощи модуля timeit.
Время выполнения скрипта median() при длине списка 
10 элементов - 0.00039420000393874943
100 элементов - 0.00027669998235069215
1000 элементов - 0.0002857999934349209

Время выполнения скрипта pyramid() при длине списка 
10 элементов - 0.028262600011657923
100 элементов - 0.2013110000116285
1000 элементов - 3.169682100007776
"""