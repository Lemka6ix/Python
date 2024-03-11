def plen(nums, k):
    if k == 0:
        return [[]]
    
    result = []
    for i, num in enumerate(nums):
        rest = nums[:i] + nums[i + 1:]
        for perm in plen(rest, k - 1):
            result.append([num] + perm)
    
    return result

print(plen([1, 2, 3], 2))
