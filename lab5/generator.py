n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def spiral_generator(matrix):
    n = len(matrix)
    x, y = n // 2, n // 2
    dx, dy = 0, 1
    step = 1
    count = 1
    yield matrix[x][y], x, y
    while count < n * n:
        for _ in range(step):
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