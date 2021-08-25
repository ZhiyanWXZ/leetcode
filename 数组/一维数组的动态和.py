from typing import List


def runningSum(nums: List[int]) -> List[int]:

    runningSum = [sum(nums[:i+1]) for i in range(len(nums))]

    return runningSum


def runningSum_origin_list(nums: List[int]) -> List[int]:

    for i in range(1, len(nums)):
        nums[i] += nums[i-1]

    return nums


if __name__ == "__main__":

    nums = [3,1,2,10,1]
    print(runningSum_origin_list(nums))
