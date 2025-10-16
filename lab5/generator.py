n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]

if n % 2 ==0:
    print('generator cannot bypass an even matrix')
    exit()

def spiral_generator(matrix):
    n = len(matrix)    # размер
    x, y = n // 2, n // 2  # центр
    dx, dy = 0, 1   # задаем направление по час. вправо
    step = 1     # Длина первого шага
    count = 1    # посетили центр
    yield matrix[x][y], x, y   # Возвращаем центральный элемент
    while count < n * n:
        for i in range(step):
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < n:
                yield matrix[x][y], x, y
                count += 1
            else:
                return
        dx, dy = dy, -dx
        if dx == 0:
            step += 1

gen = spiral_generator(matrix)
filtered = filter(lambda elem: elem[0] % 2 == (elem[1] + elem[2]) % 2, gen)
result = list(map(lambda elem: elem[0], filtered))

print(' '.join(map(str, result)))