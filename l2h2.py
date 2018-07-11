# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'
d = ''
m = ''
y = ''
i = 0

while True:
    a = date[i]
    if a == '.':
        break
    else:
        d = d + a
        i = i + 1

d1 = int(d)
print(d1)

i = i + 1
while True:
    a = date[i]
    if a == '.':
        break
    else:
        m = m + a
        i = i + 1
print(m)
m1 = int(m)


i = i + 1
y = date[i:]
print(y)
y1 = int(y)

month30 = [2, 4, 6, 9, 11]
if m1 in month30:
    max = 30
else:
    max = 31

flag = 1
if (1 <= d1 <= max) and (1 <= m1 <= 12) and (1 <= y1 <= 9999):
    flag = 0

if not(len(d) == 2 and len(m) == 2 and len(y) == 4):
    flag = 1

if flag == 0:
    print('Correct data')
else:
    print('Incorrect data')




