# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

i = 4
k = ''
b1 = ''
while True:
    a = equation[i]
    if a == 'x':
        break
    else:
        k = k + a
        i = i + 1
print(k)
print('k = ', k)

i = i + 2
if equation[i] == '+':
    sign = 1
else:
    sign = -1

i = i + 2

while True:
    a = equation[i]
    if a == '.':
        break
    else:
        b1 = b1 + a
        i = i + 1
b1 = int(b1)
#print(b1)

i = i + 1
b2 = equation[i:]
b2 = int(b2) * (pow( 10, -len(b2)))
#print(b2)
b = b1 + b2
print('b = ', b)

k = int(k)

y = x * k + b
print('y (x = {}) = {}'.format(x,y))

