print('Задание 6.')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

list = [int(i) for i in input('Введите числа через пробел: ').split()]

maximum = [(i[-1]) for i in [sorted(list)]]
first, *maximum = maximum
max_in_list = ([i for i, x in enumerate(list) if x == first])
ma, *max_in_list = max_in_list
list_max_free = list.pop(ma)

minimum = [(i[0]) for i in [sorted(list)]]
one, *minimum = minimum
min_in_list = ([i for i, x in enumerate(list) if x == one])
mi, *min_in_list = min_in_list
list_minmax_free = list.pop(mi)

d = 0
for i in list:
    d += i
print(f'Сумма введенных чисел, не учитывая наибольшего и наименьшего, равна {d}.')