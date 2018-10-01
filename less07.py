"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


def mk_string():
    str = [random.randint(1, 90) for i in range(1, 6)]
    str.sort()
    while len(str) < 9:
        str.insert(random.randint(0, 8), " ")
    return str


class Player:
    def __init__(self):
        self._card = [mk_string(), mk_string(), mk_string()]
        self.count_coincidence = 0

    def check_num(self, number):
        result = False
        for i, line in enumerate(self._card):
            for j, num in enumerate(line):
                if num == number:
                    self._card[i][j] = '-'
                    self.count_coincidence += 1
                    result = True
        return result

    def print_card(self):
        for line in self._card:
            for num in line:
                print(str(num).rjust(3), end=" ")
            print('\n')


class GameLotto:
    def __init__(self):
        self._player = Player()
        self._komputer = Player()
        self._sequence = [i for i in range(1, 91)]

    def _pull_keg(self):
        num = random.choice(self._sequence)
        self._sequence.remove(num)
        return num

    def is_end(self):
        if self._player.count_coincidence == 15:
            print("Вы выиграли!")
            return True
        elif self._komputer.count_coincidence == 15:
            print("Компьютер выиграл!")
            return True
        else:
            return False

    def start_game(self):
        while 1:
            if self.is_end():
                break
            print("Ваша карточка:")
            self._player.print_card()
            print("Карточка компьютера:")
            self._komputer.print_card()
            keg = self._pull_keg()
            print("Новый бочонок: {}, осталось: {}".format(keg, len(self._sequence)))
            answer = input("Зачеркнуть цифру? (y/n) ")
            if answer == 'y':
                if self._player.check_num(keg):
                    self._komputer.check_num(keg)
                    continue
                else:
                    print("Вы проиграли!")
                    break
            elif answer == 'n':
                if self._player.check_num(keg):
                    print("Вы проиграли!")
                    break
                else:
                    self._komputer.check_num(keg)
                    continue
            else:
                print("Некорректный выбор!")
                break


game = GameLotto()
game.start_game()


