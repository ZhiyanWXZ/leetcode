from typing import List

# BinarySearch
def searchInsert(nums: List[int], target: int) -> int:
    i = 0
    j = len(nums) - 1

    while i <= j:
        mid = (i + j) // 2
        if target < nums[mid]:
            j = mid - 1
        elif target > nums[mid]:
            i = mid + 1
        else:
            return mid
    return i

# lazy approach
# def searchInsert(nums: List[int], target: int) -> int:
#
#    if target in nums:
#        index = nums.index(target)
#    else:
#        nums.append(target)
#        nums.sort()
#        index = nums.index(target)
#    return index



if __name__ == "__main__":

    nums = [1,3,5,6]
    target = 5
    print(searchInsert(nums, target))