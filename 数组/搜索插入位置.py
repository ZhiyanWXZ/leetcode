from typing import List


def searchInsert(nums: List[int], target: int) -> int:

    for index, value in enumerate(nums):
        if value >= target:
            return index

    return len(nums)

if __name__ == "__main__":
    nums = [1]
    target = 0
    print(searchInsert(nums, target))