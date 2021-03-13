from typing import List


def removeDuplicates(nums: List[int]) -> int:
    j = 1
    length = len(nums)

    for i in range(len(nums)):
        flag = 0
        if j >= len(nums):
            break

        while j+1 < len(nums) and nums[j+1] == nums[i]:
            j = j + 1
            flag = flag + 1

        nums[i+1] = nums[j+1]
        length = length - flag
        j = j + 1
    # print(nums)
    return length


if __name__ == '__main__':
    nums = [1,1,2]
    print(removeDuplicates(nums))