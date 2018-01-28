def twoSum(nums, target):
    if len(nums) < 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [i, buff_dict[nums[i]]]
        else:
            buff_dict[target - nums[i]] = i


test_a = [2, 7, 11, 15]
print(twoSum(test_a, 9))
