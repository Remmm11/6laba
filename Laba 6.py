"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 13:
Фирма закупает К компьютеров. В магазине компьютеры N типов. Сформировать все возможные варианты покупки."""

from random import *

o = 0
computers = []
brands = ["Apple", "Asus", "Dell", "HP", "Lenovo", "Acer", "MSI", "Samsung"]


def all_combinations(arr):
    global o
    if not arr:
        return [[]]
    else:
        res = []
        for c in all_combinations(arr[1:]):
            if len(res) == 500000 and o == 0:
                o = int(input('\nКолличество возможных покупок достигло 500 000.\n'
                              'Хотите дождаться завершения работы программы? ( Да = 1 | Нет = 0 ): '))
                while o != 0 and o != 1:
                    o = int(input('\nПринимаются только значения "0" и "1": '))

                if o == 0:
                    print('\nРабота программы завершена.')
                    quit()
            res += [c, c + [arr[0]]]
        return res


try:
    a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
    while a != 0 and a != 1:
        a = int(input('\nПринимаются только значения "0" и "1": '))

    k = int(input('\nВведите кол-во покупаемых компьютеров: '))
    while k < 0:
        k = int(input('\nПринимаются только положительные числа: '))

    # Первая часть задания
    if a == 0:
        if k > 0:
            computers = [f'№ {i}: | {choice(brands)} |' for i in range(1, k + 1)]
        else:
            print('\nОчень умно! Вы решили сэкономить деньги и не купили ни одного компьютера.')
            print('\nРаботы программы завершена.')
            quit()

        combinations = sorted(all_combinations(computers), key=len)

        if len(combinations) > 30:
            b = int(input(f'\nКолличество возможных покупок равно {len(combinations)}.\n'
                          f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
            while b != 0 and b != 1:
                o = int(input('\nПринимаются только значения "0" и "1": '))

            if b == 0:
                print('\nРаботы программы завершена.')
                quit()
            else:
                print()
                for i, n in enumerate(combinations):
                    h = str(n)[1:-1].replace("'", ' ').replace(' , ', ', ')
                    print(f'{i + 1}. {h}')

        else:
            print('\nВозможные варианты покупок:')
            for i, n in enumerate(combinations):
                h = str(n)[1:-1].replace("'", ' ').replace(' , ', ', ')
                print(f'{i+1}. {h}')
    else:
        if k > 0:
            computers = [f'№ {i}: | {choice(brands)}, {randrange(10_999, 99_999, 1000)} р. |' for i in range(1, k + 1)]
        else:
            print('\nОчень умно! Вы решили сэкономить деньги и не купили ни одного компьютера.')
            print('\nРаботы программы завершена.')
            quit()

        print('\nУсложнением будет являться качество производителя.\nЕсли качество производителя низкое, то данный'
              ' производитель не будет учитываться в рассмотрении его к покупке.\nТак же у каждого компьютера есть своя'
              ' стоимость. Вывести вариант покупки с максимальной суммарной стоимостью.')

        print('\nКомпьютеры в наличии в магазине:')
        print(str(computers)[2:-1].replace("'", ' ').replace(' , ', ', '))

        if len(computers) > 1:
            b = len(computers)
            v = len(computers) // 2 - 1

            while (b - len(computers)) <= v:
                exception = []

                while len(exception) < 3:
                    r = choice(brands)
                    if r not in exception:
                        exception.append(r)

                for i, n in enumerate(computers):
                    for j in exception:
                        if j in n:
                            computers.pop(i)

            for i in exception:
                o = f'{o} {i}'
            print('\nНекачественные производители:', o[2::])

        else:
            exception = []

            while len(exception) < 3:
                r = choice(brands)
                if r not in exception:
                    exception.append(r)

            for i, n in enumerate(computers):
                for j in exception:
                    if j in n:
                        computers.pop(i)

            for i in exception:
                o = f'{o} {i}'
            print('\nНекачественные производители:', o[2::])

        if len(computers) > 0:
            print('\nКомпьютеры подлежащие выбору:')
            print(str(computers)[2:-1].replace("'", ' ').replace(' , ', ', '))

            combinations = sorted(all_combinations(computers), key=len)[1:]

            if len(combinations) > 30:
                b = int(input(f'\nКолличество возможных покупок равно {len(combinations)}.\n'
                              f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
                while b != 0 and b != 1:
                    o = int(input('\nПринимаются только значения "0" и "1": '))

                if b == 1:
                    print()
                    for i, n in enumerate(combinations):
                        h = str(n)[1:-1].replace("'", ' ').replace(' , ', ', ')
                        print(f'{i + 1}. {h}')

            else:
                print('\nВозможные варианты покупок:')
                for i, n in enumerate(combinations):
                    h = str(n)[1:-1].replace("'", ' ').replace(' , ', ', ')
                    print(f'{i + 1}. {h}')

            s = [int(str(i)[-10:-5]) for i in computers]

            print('\nВариант самой дорогой покупки: ')
            print(f'Сумма покупки: {sum(s)} руб.')
            print(str(computers[::-1])[4:-2].replace("'", ' ').replace(' , ', ', '))

        else:
            print('\nКажется, сегодня мы остались без покупок.')

    print('\nРаботы программы завершена.')
except ValueError:
    print(f'\nПерезапустите программу и введите число, а не символ.')
