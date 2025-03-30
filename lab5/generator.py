from functools import reduce

def spiral_matrix_generator(matrix, start_direction="right"):
    """
    Генератор, обходящий элементы матрицы по спирали, начиная с центра,
    и возвращающий только те элементы, четность которых совпадает с четностью
    суммы их индексов.

    Args:
        matrix: Двумерный список (матрица).
        start_direction: Направление старта спирали ('right', 'left', 'up', 'down').

    Yields:
        Значения элементов матрицы, удовлетворяющих условиям обхода и четности.
    """

    if not matrix or not matrix[0]:
        return  # Пустая матрица

    rows, cols = len(matrix), len(matrix[0])
    center_row, center_col = rows // 2, cols // 2

    # Обработка случаев, когда матрица имеет нечетное количество строк/столбцов.
    # В этих случаях центр смещается.
    if rows % 2 != 0:
        center_row = rows // 2
    else:
        center_row = rows // 2 -1 #Смещаем центр для четных матриц

    if cols % 2 != 0:
        center_col = cols // 2
    else:
        center_col = cols // 2 -1  #Смещаем центр для четных матриц


    row, col = center_row, center_col
    dr, dc = 0, 1  # Направление: вправо (по умолчанию)

    if start_direction == "left":
        dr, dc = 0, -1
    elif start_direction == "up":
        dr, dc = -1, 0
    elif start_direction == "down":
        dr, dc = 1, 0
    elif start_direction != "right":
         raise ValueError("Недопустимое направление. Допустимые значения: 'right', 'left', 'up', 'down'")



    visited = set()
    num_visited = 0
    max_elements = rows * cols  # Максимальное количество элементов, которые нужно посетить


    while num_visited < max_elements:
        if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
            if (matrix[row][col] % 2) == ((row + col) % 2):  # Проверка четности
                yield matrix[row][col]
            visited.add((row, col))
            num_visited +=1


        # Попытка сменить направление
        new_dr, new_dc = -dc, dr # Поворот на 90 градусов по часовой стрелке
        new_row, new_col = row + new_dr, col + new_dc

        if not (0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited): #Если нельзя повернуть
            new_dr, new_dc = dr, dc #Оставляем направление без изменений
            new_row, new_col = row + new_dr, col + new_dc # Сдвигаем в текущем направлении
        
        # Сдвигаемся в выбранном направлении
        row, col = new_row, new_col
        dr, dc = new_dr, new_dc


# Пример использования:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


# Используем filter для отбора только четных чисел из сгенерированной последовательности
spiral_even = filter(lambda x: x % 2 == 0, spiral_matrix_generator(matrix, "down")) #Начинаем обход снизу, от центра
print(list(spiral_even))

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

spiral_odd = filter(lambda x: x % 2 != 0, spiral_matrix_generator(matrix2, "up"))
print(list(spiral_odd))

matrix3 = [
    [1, 2],
    [3, 4]
]

spiral_all = spiral_matrix_generator(matrix3, "right")
print(list(spiral_all))  # Выведет [4, 2]
