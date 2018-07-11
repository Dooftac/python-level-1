# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list = []
repeat = []
while True:
    a = input('fill the first list (end to finish)')
    if a != 'end':
        list.append(int(a))
    else:
        break

print(list)

for i in range(len(list)):
    if (list[i] in list[(i+1):]) and not (list[i] in repeat):
        repeat.append(list[i])

i=0


while i < len(list):
    if list[i] in repeat:
        list.pop(i)
    else:
        i = i + 1



print(list)
#print(repeat)
