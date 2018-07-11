# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1=[]
list2=[]

while True:
    a=input('fill the first list (0-end)')
    if a!='0':
        list1.append(a)
    else:
        break

while True:
    a = input('fill the second list (0-end)')
    if a != '0':
        list2.append(a)
    else:
        break

print(list1)
print(list2)

ll = len(list1)
i = 0
while i < ll:
    if list1[i] in list2:
        a = list1.pop(i)
        ll = ll-1
    else:
        i = i+1

print(list1)


