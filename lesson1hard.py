# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

name1 = input("Ведите имя: ")
name2 = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
w = int(input('Введите вес: '))

print(name1, ' ', name2, ' ', 'возраст ', age, 'вес ', w)

if age<30 and w>=50 and w<=120:
    print('Пациент в хорошем состоянии')

elif age>40 and (w<50 or w>120):
    print('Пациенту требуется врачебный осмотр')

elif age>30 and (w<50 or w>120):
    print('Пациенту требуется начать вести правильный образ жизни')


