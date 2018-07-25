# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
for number in range(1,10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(number))
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Файл не найден!')