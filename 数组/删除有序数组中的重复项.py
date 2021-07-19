from typing import List

# code myself
# def removeDuplicates(nums: List[int]) -> int:
#
#     for i in range(len(nums)):
#         indexes = []
#         for j in range(i+1, len(nums)):
#             if j >= len(nums):
#                 break
#             if nums[j] == nums[i]:
#                 indexes += [j]
#                 print(indexes)
#             else:
#                 break
#
#         for i in indexes[::-1]:
#             del nums[i]
#     return len(nums)


# learn from comments
def removeDuplicates(nums: List[int]) -> int:

    if len(nums) == 0:
        return 0
    index = 1
    while index < len(nums):
        if nums[index] == nums[index-1]:
            del nums[index-1]
        else:
            index += 1
    return len(nums)

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)
