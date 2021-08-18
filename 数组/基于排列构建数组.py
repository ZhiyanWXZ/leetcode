from typing import List


def buildArray(nums: List[int]) -> List[int]:

    ans = []
    for i in range(len(nums)):
        ans.append(nums[i])
    for i in range(len(nums)):
        index = nums[i]
        ans[i] = nums[index]
    return ans


if __name__ == '__main__':

    nums = [5,0,1,2,3,4]
    buildArray(nums)