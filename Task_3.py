print('Задание 3.')

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

list = [int(i) for i in input('Введите числа через пробел: ').split()]

maximum = [(i[-1]) for i in [sorted(list)]]
minimum = [(i[0]) for i in [sorted(list)]]
first, *maximum = maximum
one, *minimum = minimum

max_in_list = ([i for i, x in enumerate(list) if x == first])
min_in_list = ([i for i, x in enumerate(list) if x == one])

ma, *max_in_list = max_in_list
mi, *min_in_list = min_in_list

list[mi], list[ma] = list[ma], list[mi]

print('Ваши числа, большее и меньшее переставлены местами: ', ' '.join(str(i) for i in list))