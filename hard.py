# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копия файла")
    print("rm <file_name> - удалить файл")
    print("ls - полный путь текущей директории")
    print("cd <relative_path> - смена директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        dir_path = os.path.join(os.getcwd(), dir_name)
        f = open(dir_path, 'r', encoding='UTF-8')
        data = f.readlines()
        f.close()
        path = os.path.join(os.getcwd(), 'копия.py')
        f = open(path, 'w', encoding='UTF-8')
        for string in data:
            f.write(string)
        f.close
    except FileNotFoundError:
        print('Файл не найден!')

def del_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.remove(dir_path)
    except FileNotFoundError:
        print('Файл не найден!')

def full_path():
    print(os.getcwd())

def change_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
    except FileNotFoundError:
        print('Папка не найдена')

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "ls": full_path,
    "cd": change_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.