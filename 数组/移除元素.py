from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    i = 0
    j = 0
    new_num = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            new_num += [nums1[i]]
            i += 1
        else:
            new_num += [nums2[j]]
            j += 1
    while i < len(nums1):
        new_num += [nums1[i]]
        i += 1
    while j < len(nums2):
        new_num += [nums2[j]]
        j += 1
    if len(new_num) % 2 == 1:
        return float(new_num[int(len(new_num)/2)])
    else:
        return float((new_num[int(len(new_num)/2-1)] + new_num[int(len(new_num)/2)]) / 2)

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    print(findMedianSortedArrays(nums1, nums2))


# python way with bulit-in function
# new_num = nums1 + nums2
# new_num.sort()
# if len(new_num) % 2 == 1:
#     return float(new_num[int(len(new_num) / 2)])
# else:
#     return float((new_num[int(len(new_num) / 2 - 1)] + new_num[int(len(new_num) / 2)]) / 2)

