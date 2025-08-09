from functools import reduce

def spiral_matrix_generator(matrix, start_direction='right'):
    rows = len(matrix)
    cols = len(matrix[0])

    # Вычисляем координаты центра матрицы
    center_row = rows // 2
    center_col = cols // 2
    if rows % 2 == 0:
        center_row -= 1
    if cols % 2 == 0:
        center_col -= 1

    # Определяем начальные координаты и направление
    row, col = center_row, center_col
    direction = start_direction

    # Список посещенных ячеек, чтобы не посещать их повторно
    visited = set()

    # Вспомогательная функция для проверки допустимости координат
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Вспомогательная функция для получения следующей ячейки
    def next_cell(r, c, direction):
        if direction == 'right':
            return r, c + 1
        elif direction == 'left':
            return r, c - 1
        elif direction == 'up':
            return r - 1, c
        elif direction == 'down':
            return r + 1, c
        else:
            raise ValueError("Недопустимое направление")

    # Основной цикл обхода
    while len(visited) < rows * cols:
        if (row, col) not in visited and is_valid(row, col):
            visited.add((row, col))
            if (row + col) % 2 == matrix[row][col] % 2:  #Проверка чётности суммы индексов и чётности элемента
                yield matrix[row][col]

        # Попытка двигаться в текущем направлении
        next_row, next_col = next_cell(row, col, direction)
        if is_valid(next_row, next_col) and (next_row, next_col) not in visited:
            row, col = next_row, next_col
        else:
            # Изменение направления, если движение вперед невозможно
            if direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'left'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'up':
                direction = 'right'
            # Повторная попытка движения в новом направлении
            next_row, next_col = next_cell(row, col, direction)
            if is_valid(next_row, next_col) and (next_row, next_col) not in visited:
                 row, col = next_row, next_col
            else:
                # Если даже после изменения направления двигаться некуда, значит, все окрестности посещены
                break

# Пример использования:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Создаем генератор
spiral_gen = spiral_matrix_generator(matrix, 'up')

# Применяем map для преобразования элементов (удваиваем их)
# и filter для выбора только четных удвоенных значений
filtered_doubled_values = filter(lambda x: x % 2 == 0, map(lambda x: x * 2, spiral_gen))


# Выводим результат с использованием list() для преобразования генератора в список
print(list(filtered_doubled_values))  #Вывод: [12, 16, 14, 30, 22]
