# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

list = []
n = int(input('number of elements:'))

for i in range(n):
    a = random.randint(-100, 100)
    list.append(a)

print(list)