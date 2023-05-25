"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 13:
Фирма закупает К компьютеров. В магазине компьютеры N типов. Сформировать все возможные варианты покупки."""

from random import choice, randrange

maxs = d = 0
combr = []
maxstr = []
computers = []
exception = []
combinations = []
BRANDS = ['Apple', 'Asus', 'Dell', 'HP', 'Lenovo', 'Acer', 'MSI', 'Samsung']


def product(*args, repeat=1):
    # если нет аргументов, возвращаем пустой список
    pools = list(map(tuple, args)) * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


try:
    cntcomps = int(input('\nВведите кол-во покупаемых компьютеров: '))
    while cntcomps < 0:
        cntcomps = int(input('\nПринимаются только положительные числа: '))
    if not cntcomps:
        print('\nОчень умно! Вы решили сэкономить деньги и не купили ни одного компьютера.')
        quit()

    cnttips = int(input('\nВведите кол-во типов компьютеров: '))
    while cnttips < 0:
        cnttips = int(input('\nПринимаются только положительные числа: '))
    if not cnttips:
        print('\nКажется, сегодня мы остались без покупок.')
        quit()

    try:
        switch = int(input('\nЗапустить усложнённую версию программы? ( Нет = 0 | Да = 1 ): '))
        while switch != 0 and switch != 1:
            switch = int(input('\nПринимаются только значения "0" и "1": '))
    except ValueError:
        switch = 0

    # Первая часть задания
    if not switch:
        computers = [f'№ {i}: {choice(BRANDS)}' for i in range(1, cnttips + 1)]

    if switch:
        print('\nУсложнением будет являться качество производителя.\nЕсли качество производителя низкое, то данный'
              ' производитель не будет учитываться в рассмотрении его к покупке.\nТак же у каждого компьютера есть своя'
              ' стоимость. Вывести вариант покупки с максимальной суммарной стоимостью.')

        computers = [f'{choice(BRANDS)} ({randrange(10999, 99999, 1000)} р.)' for i in range(1, cnttips + 1)]

        print('\nКомпьютеры в магазине:')
        print(str(computers)[2:-1].replace("'", ''))

        if len(computers) > 1:
            b = len(computers)

            while (b - len(computers)) <= (b // 2 - 1):
                r = choice(BRANDS)
                if r not in exception:
                    exception.append(r)

                for i, var in enumerate(computers):
                    for j in exception:
                        if j in var:
                            computers.pop(i)
            else:
                for i in exception:
                    d = f'{d}, {i}'
                print('\nНекачественные производители:', d[2::])

        else:
            while len(exception) < 3:
                r = choice(BRANDS)
                if r not in exception:
                    exception.append(r)

            for i, var in enumerate(computers):
                for j in exception:
                    if j in var:
                        computers.pop(i)

            for i in exception:
                d = f'{d} {i}'
            print('\nНекачественные производители:', d[2::])

    if computers:
        print('\nКомпьютеры подлежащие выбору:')
        print(str(computers)[2:-1].replace("'", ''))
    else:
        print('\nКажется, сегодня мы остались без покупок.')
        quit()

    for i, var in enumerate(product(computers, repeat=cntcomps)):
        s = 0
        b = {}

        if (cntcomps > 4 and len(computers) > 8) or (cntcomps > 9 or len(computers) > 12) and not d:
            d = int(input(f'\nВы ввели большие значения K или N, работа программы может занять существенное '
                          f'время. Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
            while not d and d:
                d = int(input('Принимаются только значения "0" и "1": '))
            if not d:
                quit()

        for j in sorted(var):
            if j in b:
                b[j] = b[j] + 1
            else:
                b[j] = 1
            if switch == 1:
                s += int(j[-9:-4])
        if b not in combr:
            combinations.append(var)

        if switch == 1:
            if s >= maxs:
                maxs = s
                maxstr = var

        combr.append(b)

    b = 1
    if len(combinations) > 30:
        b = int(input(f'\nКолличество возможных покупок равно {len(combinations)}.\n'
                      f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
        while not b and b:
            b = int(input('\nПринимаются только значения "0" и "1": '))

    if b:
        print('\nВозможные варианты покупок:')
        for i, var in enumerate(sorted(combinations, key=len)):
            h = str(var)[1:-2].replace("'", '').replace(', ', ' | ')
            print(f'{i + 1}. {h}')

    if switch:
        print('\nВариант самой дорогой покупки: ')
        print(f'Сумма покупки: {maxs} руб.')
        print(str(maxstr[::-1])[2:-2].replace("'", '').replace(', ', ' | '))

except ValueError:
    print(f'\nПерезапустите программу и введите нужную цифру.')
