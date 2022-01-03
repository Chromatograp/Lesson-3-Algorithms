from collections import Counter

print('Задание 4.')

# 4. Определить, какое число в массиве встречается чаще всего.

list = [int(i) for i in input('Введите числа через пробел. Желательно, чтобы хотя бы одно из них повторялось: ').split()]

num = Counter(list)

max_val = None
max_key = -1
for i in num:
    if max_val is None or max_val < num[i]:
        max_val = num[i]
        max_key = i

print(f'В вашем списке чаще всего встречается число {max_key}')