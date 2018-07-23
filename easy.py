import os

def go_to(dir_name):
    new_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(new_path)
        print('Директория успешно сменена')
    except FileNotFoundError:
        print('Папка не найдена')

def show():
    list = os.listdir(os.getcwd())
    print(list)

def delete(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Папка успешно удалена')
    except FileNotFoundError:
        print('Папка не найдена!')

def create(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Папка успешно создана')
    except FileExistsError:
        print('Такая папка уже существует')

