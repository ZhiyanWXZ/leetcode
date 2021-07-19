# class Solution(object):
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #暴力枚举，忽略了当i与j匹配时，i之前的数已经和i匹配过，所以不需要重复匹配
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i== j:
                continue
            if nums[i] + nums[j] == target:
                out = [i,j]
                return out


def hash_way(nums, target):
    hash_dict = {}
    for index, value in enumerate(nums):
        result = target - value
        if result in hash_dict.keys():
            return index, hash_dict[result]
        else:
            hash_dict[value] = index
        print(hash_dict)


if __name__ == "__main__":

    nums = [3, 3]
    target = 6
    print(hash_way(nums, target))