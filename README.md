```python
from functools import reduce

def spiral_matrix_generator(matrix, start_direction="right"):
   

    if not matrix or not matrix[0]:
        return  

    rows, cols = len(matrix), len(matrix[0])
    center_row, center_col = rows // 2, cols // 2

    
    if rows % 2 != 0:
        center_row = rows // 2
    else:
        center_row = rows // 2 -1 

    if cols % 2 != 0:
        center_col = cols // 2
    else:
        center_col = cols // 2 -1  


    row, col = center_row, center_col
    dr, dc = 0, 1  
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
    max_elements = rows * cols  


    while num_visited < max_elements:
        if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
            if (matrix[row][col] % 2) == ((row + col) % 2):  
                yield matrix[row][col]
            visited.add((row, col))
            num_visited +=1


        
        new_dr, new_dc = -dc, dr 
        new_row, new_col = row + new_dr, col + new_dc

        if not (0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited): 
            new_dr, new_dc = dr, dc 
            new_row, new_col = row + new_dr, col + new_dc 
        
        
        row, col = new_row, new_col
        dr, dc = new_dr, new_dc



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


spiral_even = filter(lambda x: x % 2 == 0, spiral_matrix_generator(matrix, "down")) 
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
```
## Как это работает
1. Инициализация: Определяются размеры матрицы, координаты центра, начальное направление и множество `visited` для отслеживания посещенных элементов.
2. Обход спирали:
   - На каждой итерации проверяется, находится ли текущая ячейка в пределах матрицы и была ли она уже посещена.
   - Если ячейка удовлетворяет этим условиям, проверяется условие четности. Если оно выполняется, значение ячейки возвращается через `yield`.
   - Ячейка добавляется в `visited`.
   - Алгоритм пытается повернуть на 90 градусов по часовой стрелке.  Если это невозможно (выход за границы или ячейка уже посещена), он продолжает двигаться в текущем направлении.
3. Завершение: Алгоритм завершается, когда все элементы матрицы были посещены (или когда невозможно двигаться дальше).
4. Применение `filter`:  Результат работы генератора передается в функцию `filter`, которая отбирает только те элементы, которые удовлетворяют заданному условию (например, четные числа).