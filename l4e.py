# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

list1 = [1, -5, 7, 10, 0]
list2 = [element ** 2 for element in list1]
print(list2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list1 = ['kiwi', 'apple', 'pineapple', 'banana', 'kiwi']
list2 = ['apple', 'orange', 'mango', 'kiwi']
list3 = [fruit for fruit in list1 if list2.count(fruit) >= 1]
list3 = list(set(list3))
print(list3)

# Задание-3:
list = [1,6,4,3,3.9,4.4,12,14]
list2 = [element for element in list if (element % 3 == 0 and element > 0 and element % 4 != 0)]
print(list2)
