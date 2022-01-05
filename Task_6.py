print('Задание 6.')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

list = [int(i) for i in input('Введите числа через пробел: ').split()]

# Находим в списке максимальный элемент:
maximum = [(i[-1]) for i in [sorted(list)]]
# Распаковываем его значение из списка:
first, *maximum = maximum
# Находим его индекс:
max_in_list = ([i for i, x in enumerate(list) if x == first])
# Распаковываем значение индекса:
ma, *max_in_list = max_in_list
# Удаляем значение из введенного списка:
list_max_free = list.pop(ma)

# Находим в списке минимальный элемент:
minimum = [(i[0]) for i in [sorted(list)]]
# Распаковываем его из списка:
one, *minimum = minimum
# Находим его индекс:
min_in_list = ([i for i, x in enumerate(list) if x == one])
# Распаковываем значение индекса:
mi, *min_in_list = min_in_list
# Удаляем элемент из введенного списка:
list_minmax_free = list.pop(mi)

summa = 0
for i in list:
    """Находим сумму оставшихся элементов списка, поочередно прибавляя их к summa"""
    summa += i
print(f'Сумма введенных чисел, не учитывая наибольшего и наименьшего, равна {summa}.')