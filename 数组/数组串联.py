from typing import List


def getConcatenation(nums: List[int]) -> List[int]:

    # ans = [num for num in nums]
    # for num in nums:
    #     ans.append(num)

    # return ans
    return nums + nums


if __name__ == '__main__':

    nums = [1, 2, 1]
    print(getConcatenation(nums))