# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
path = os.path.join(os.getcwd(), 'copy.py')
f = open(path, 'r', encoding='UTF-8')
data = f.readlines()
f.close()
path = os.path.join(os.getcwd(), 'copy1.py')
f = open(path, 'w', encoding='UTF-8')
for string in data:
    f.write(string)
f.close

