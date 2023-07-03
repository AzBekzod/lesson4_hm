"""
Напишите функцию для транспонирования матрицы
Пример:
[[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
"""


def transpose_matrix(m):
    num_rows = len(m)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    transposed = []
    for col in range(num_cols):
        transposed.append([matrix[r][col] for r in range(num_rows)])

    return transposed


matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print('\t'.join(str(element) for element in row))
