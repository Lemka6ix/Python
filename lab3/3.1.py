def plen(nums, k):
    if k == 0:
        return [[]]
    
    if k > len(nums):
        return []
    result = []
    for i in range(len(nums)):
        current_nums = nums[i]
        remain_nums = nums[:i] + nums[i+1:]
        smal_perm = plen(remain_nums, k-1)

        for i in smal_perm:
            result.append([current_nums] + i)
    return result

print(plen([1, 2, 3], 2))
