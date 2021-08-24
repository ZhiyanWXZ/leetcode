from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode:

    head = TreeNode(nums[0])

    for num in nums:
        if num == head.val:
            continue
        node = TreeNode(num)
