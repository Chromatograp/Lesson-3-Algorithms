print('Задание 3.')

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

list = [int(i) for i in input('Введите числа через пробел: ').split()]

# Из списка, введенного пользователем, получаем максимальное и минимальное число, воспользовавшись сортировкой по
# возрастанию:
maximum = [(i[-1]) for i in [sorted(list)]]
minimum = [(i[0]) for i in [sorted(list)]]

# Распаковываем полученные числа из списков:
most, *maximum = maximum
least, *minimum = minimum

# Получаем индексы чисел:
max_in_list = ([i for i, x in enumerate(list) if x == most])
min_in_list = ([i for i, x in enumerate(list) if x == least])

# Распаковываем индексы из списков:
ma, *max_in_list = max_in_list
mi, *min_in_list = min_in_list

# Переставляем местами элементы с полученными индексами:
list[mi], list[ma] = list[ma], list[mi]

# Добавляем полученные индексы в список:
print('Ваши числа, большее и меньшее переставлены местами: ', ' '.join(str(i) for i in list))