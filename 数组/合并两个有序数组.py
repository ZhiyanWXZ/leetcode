from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return None
    if m == 0:
        i = 0
        while i < n:
            nums1[i] = nums2[i]
            i += 1
        return None
    i = 0
    while i < n:

        low = 0
        high = m - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums2[i] > nums1[mid]:
                low = mid + 1
            else:
                high = mid - 1
        j = m - 1
        while j > high:
            nums1[j+1] = nums1[j]
            j -= 1
        nums1[high+1] = nums2[i]
        m += 1
        i += 1
        print(nums1)


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    merge(nums1, m, nums2, n)
    print(nums1)
