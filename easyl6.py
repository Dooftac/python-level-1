# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police=0):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = bool(is_police)

    def go(self):
        print('Car {} started driving'.format(self.name))

    def stop(self):
        print('Car {} stopped'.format(self.name))

    def turn(self, direction):
        print('Car {} turned {}'.format(self.name, direction))

    def info(self):
        print(self.name, self.color, self.speed, self.is_police)


class TownCar(Car):
    def __init__(self, speed, color, name, age, is_police = 0):
        super().__init__(speed, color, name)
        self.age = age

    def info(self):
        super().info()
        print('age:', self.age)

class SportCar(Car):
    def __init__(self, speed, color, name, acceleration, is_police = 0):
        super().__init__(speed, color, name)
        self.acc = acceleration

    def turbina(self, increase):
        self.acc += increase

    def info(self):
        super().info()
        print('acceleration:', self.acc)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = 1):
        super().__init__(speed, color, name, is_police)

car1 = Car(70, 'red', 'Bibika', 0)
car1.turn('right')

car2 = PoliceCar(120, 'black', 'Officer')
car2.turn('left')

car3 = TownCar(100, 'white', 'Жигули',3)
car3.info()
