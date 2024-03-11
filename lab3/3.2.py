def compe(i):
    if i == 0:
        return 0
    else:
        return i * compe(i - 1) + 1 / i

index = 5
resultrec = compe(index)
print(f"Результат вычисления x с индексом {index} с рекурсией: {resultrec}")
