from typing import List

# 暴力
# def twoSum(numbers: List[int], target: int) -> List[int]:
#
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return [i+1, j+1]
#             if numbers[j] >= target:
#                 break


# 双指针法
# def twoSum(numbers: List[int], target: int) -> List[int]:
#
#     i = 0
#     j = len(numbers) - 1
#     while True:
#         if numbers[i] + numbers[j] == target:
#             return [i+1, j+1]
#         elif numbers[i] + numbers[j] < target:
#             i = i + 1
#         else:
#             j = j - 1


# 二叉查找
def twoSum(numbers: List[int], target: int) -> List[int]:

    for index, number in enumerate(numbers):
        find = target - number
        low = index + 1
        high = len(numbers) - 1

        while low <= high:
            mid = int((low + high) / 2)
            if numbers[mid] == find:
                return [index+1, high+1]
            elif numbers[mid] < find:
                low = mid + 1
            else:
                high = mid - 1


if __name__ == '__main__':

    numbers = [-1, 0]
    target = -1
    print(twoSum(numbers, target))
