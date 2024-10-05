nums = [2, 7, 11, 15, 6, 3]
target = 9
'''def target_finder(nums):

    targets = []
    for i in nums:
        for j in nums:
            if i + j == target:
                targets.append([i, j])
    return targets
            
result = target_finder(nums)
print(result)'''

#_____________________________________________________________

def target_finder(nums, target=0):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([nums[i], nums[j]])

    return result

result = target_finder(nums, target)
print(result)

