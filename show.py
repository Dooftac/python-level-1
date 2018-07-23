# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
list = os.listdir(os.getcwd())
for element in list:
    if not '.' in element:
        print(element)