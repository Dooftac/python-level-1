# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
b=b+a
a=b-a
b=b-a
print('Первое число теперь ', a)
print('Второе число теперь ', b)