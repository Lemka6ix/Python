def sesh(i):
    result = 0
    for j in range(1, i + 1):
        result = j * result + 1 / j
    return result

index = 5
resic = sesh(index)
print(f"Результат вычисления x с индексом {index} без рекурсии: {resic}")
