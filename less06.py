#easy
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
print("Задача 1.1-1.2")


class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self._name))

    def stop(self):
        print('Машина {} остановилась'.format(self._name))

    def turn(self, direction):
        print('Машина {} поехала {}'.format(self._name, direction))


class TownCar(Car):
    def __init__(self, speed=90, color='blue', name='town car', is_police=False):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed=160, color='red', name='sport car', is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed=40, color='yellow', name='work car', is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed=60, color='white', name='police car', is_police=True):
        super().__init__(speed, color, name, is_police)


townCar = TownCar()
townCar.turn('налево')
policeCar = PoliceCar()
policeCar.go()
workCar = WorkCar()
workCar.stop()

#normal

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
print("Задача 2.1")


class Person:
    def __init__(self, name='guest', health=100, damage=50, armor=0.7):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor

    def calculate_damage(self, armor):
        return self._damage // armor

class Player(Person):
    def __init__(self, name='guest', health=100, damage=50, armor=0.7):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name='guest', health=60, damage=50, armor=0.7):
        super().__init__(name, health, damage, armor)

class Game :
    def __init__(self):
        self._player = Player()
        self._enemy = Enemy()

    def attack(self, who_attack, who_defend):
        damage = who_attack.calculate_damage(who_defend._armor)
        who_defend._health -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(who_attack._name, who_defend._name, damage,
                                                                    who_defend._health))

    # Функция старта игры, никаких аргументов не принимает.
    def start_game(self):
        self._player._name = input("Введите имя первого игрока:")
        self._enemy._name = input("Введите имя второго игрока:")

        # Запоминаем кто последний атаковал
        last_attacker = self._player
        while self._player._health > 0 and self._enemy._health > 0:
            if last_attacker == self._player:
                self.attack(self._enemy, self._player)
                last_attacker = self._enemy
            else:
                self.attack(self._player, self._enemy)
                last_attacker = self._player

        if self._player._health > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


game = Game()
game.start_game()

#hard
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
print("Задание 3.1")


class Toy:
    def __init__(self, type, name, color):
        self._type = type
        self._name = name
        self._color = color


class Factory:
    def __init__(self, type, name='None', color='None'):
        self._type = type
        self._name = name
        self._color = color

    def buy_raw(self):
        print("Закупка сырья")
    def tailoring_toy(self):
        print("Пошив игрушки")
    def colouring_toy(self):
        print("Покраска игрушки")
    def release_toy(self):
        print("Выпуск игрушки:")
        return Toy(self._type, self._name, self._color)


factory = Factory("soft_toy", "Умка", "белый")
factory.buy_raw()
factory.tailoring_toy()
factory.colouring_toy()
new_toy = factory.release_toy()
print(new_toy._type, new_toy._name, new_toy._color )

print("Задание 3.2")


class Bear(Toy):
    def __init__(self, type='soft_toy', name='Умка', color='white'):
        super().__init__(type, name, color)


class Car(Toy):
    def __init__(self, type='car', name='McQueen', color='red'):
        super().__init__(type, name, color)


class Doll(Toy):
    def __init__(self, type='doll', name='Маша', color='multi'):
        super().__init__(type, name, color)


class FactoryNew(Factory):
    def __init__(self, type):
        super().__init__(type)

    def release_toy(self):
        print("Выпуск игрушки:")
        if self._type == 'soft_toy':
            return Bear()
        elif self._type == 'car':
            return Car()
        elif self._type == 'doll':
            return Doll()


factory_new = FactoryNew('car')
factory_new.buy_raw()
factory_new.tailoring_toy()
factory_new.colouring_toy()
new_toy = factory_new.release_toy()
print(new_toy._type, new_toy._name, new_toy._color)

