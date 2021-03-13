class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #暴力枚举，忽略了当i与j匹配时，i之前的数已经和i匹配过，所以不需要重复匹配
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i== j:
                    continue
                if nums[i] + nums[j] == target:
                    out = [i,j]
                    return out