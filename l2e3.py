# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list=[]
while True:
    a = input('fill the list (print end to stop)')
    if a != 'end':
        list.append(int(a))
    else:
        break

clon = []
for i in range(len(list)):
    if list[i] % 2 == 0:
        clon.append(list[i]/4)
    else:
        clon.append(list[i]*2)

print(list)
print(clon)