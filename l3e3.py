# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_length(*str):
    return max(str, key = len)

print(max_length('igor', 'kdld;sj', 'cat', 'xyxyxyxyxyxyxyxy'))