def pepi(nums, k):
    result = []
    stick = [(list(nums), [])]

    while stick:
        curr, permutation = stick.pop()
        if len(permutation) == k:
            result.append(permutation)
        else:
            for i in range(len(curr)):
                next_perm = permutation + [curr[i]]
                next_remain = curr[:i] + curr[i+1:]
                stick.append((next_remain, next_perm))

    return result

result = pepi([1, 2, 3], 2)
print(result)
