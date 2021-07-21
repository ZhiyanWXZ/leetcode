from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = len(nums) - 1

    while i >= 0:

        if nums[i] == val:
            del nums[i]
        i -= 1

    return len(nums)


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(removeElement(nums, val))
