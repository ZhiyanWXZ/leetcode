from typing import List

# python  the difference of del and remove:
# 1、del deletes the member according to the index of the list,not the value.
# 根据索引进行删除，不会根据值进行删除
# 2、function remove deletes the first occurence of the value in the list, also, it delete the member by the value.
# list中首次出现的元素删除，按值删除。但在程序中，使用的是下标遍历的方法，在删除一个元素后，下标和实际将要访问的元素发生错位，导致错误
def removeElement(nums: List[int], val: int) -> int:

    while val in nums:
            nums.remove(val)
    return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2

# in this way, del can not delete the target value
for num in nums:
    if num == val:
        del num
print(nums)
print("------------------------")

for i in range(len(nums)):
    if nums[i] == val:
        del nums[i]
    print(nums)
# print(nums)

