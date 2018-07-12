# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
list = []
while True:
    a = input('fill the first list (end to finish)')
    if a != 'end':
        list.append(int(a))
    else:
        break

clon = []
for i in range(len(list)):

    if list[i] > 0:
        if pow(list[i], 0.5) % 1 == 0:
            clon.append( int(pow(list[i], 0.5)))

print(list)
print(clon)
