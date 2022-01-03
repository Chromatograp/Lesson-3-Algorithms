print('Задание 9.')

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

n, m = int(input('Введите количество строк матрицы: ')), int(input('Введите количество столбцов матрицы: '))
matrix = []
for i in range(n):
    matrix += [[input('Введите матрицу по одной цифре: ') for _ in range(m)]]
print(f'Ваша матрица:\n{matrix}')

max = matrix[0]
for i in matrix:
    for j, k in enumerate(i):
        if k > max[j]:
            max[j] = k

print(f'Максимальные числа каждого столбца:\n{max}')