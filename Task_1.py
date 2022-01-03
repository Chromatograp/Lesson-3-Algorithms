from itertools import zip_longest

print('Задание 1.')

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

n = ([i for i in range(2, 100)])


def nod(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def nok(a, b):
    return a * b // nod(a, b)


d = 2
div = []
for i in range(2, 10):
    d = nok(d, i)
    div.append(d)

division = ([i for i in div if i % 9 == 0])

num, *division = division

if d in n:
    print(f'{num} делится без остатка на все числа от 2 до 9.')
else:
    print(f'Только {num} делится на все числа в диапазоне от 2 до 9.')
