from typing import List


def majorityElement(nums: List[int]) -> int:

    count = {}
    for num in nums:
        if num in count.keys():
            count[num] += 1
        else:
            count[num] = 1
    for i in count.keys():
        if count[i] > int(len(nums)/2):
            return i


if __name__ == '__main__':

    nums = [6,5,5]
    print(majorityElement(nums))