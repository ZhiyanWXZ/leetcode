from typing import List


def numIdenticalPairs(nums: List[int]) -> int:

    sum = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                sum += 1

    return sum


def numIdenticalPairs_hash(nums: List[int]) -> int:

    sum = 0
    count = {}
    for num in nums:
        if num in count.keys():
            count[num] += 1
        else:
            count[num] = 1
    for i in count.keys():
        if count[i] == 1:
            continue
        else:
            sum += count[i]*(count[i]-1) / 2
    return int(sum)


if __name__ == "__main__":

    nums = [1,1,1,1]
    print(numIdenticalPairs_hash(nums))