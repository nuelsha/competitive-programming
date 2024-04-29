def twoSum(nums, target):
    ans = {}
    for i, n in enumerate(nums):
        diff = target - n 
        if diff in ans:
            return [ans[diff], i]
        else:
            ans[n] = i

print(twoSum([1,2,3,4,5], 9))