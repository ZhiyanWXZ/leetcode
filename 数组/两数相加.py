# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# true answer
# class Solution:

def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:

    head = ListNode(0, None)
    node = head
    carry = 0
    while l1 is not None and l2 is not None:
        value = l1.val + l2.val + carry
        carry = 0
        if value >= 10:
            carry = 1
            value -= 10
        new_node = ListNode(value, None)
        node.next = new_node
        node = new_node
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        value = l1.val + carry
        carry = 0
        if value >= 10:
            carry = 1
            value -= 10
        new_node = ListNode(value, None)
        node.next = new_node
        node = new_node
        l1 = l1.next

    while l2 is not None:
        value = l2.val + carry
        carry = 0
        if value >= 10:
            carry = 1
            value -= 10
        new_node = ListNode(value, None)
        node.next = new_node
        node = new_node
        l2 = l2.next

    head = head.next
    return head


if __name__ == '__main__':
    l1 = ListNode(1, None)
    l2 = ListNode(1, None)
    result = addTwoNumbers(l1, l2)
    print(result.val)

# first try
# class Solution:
#
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # value1 = 0
        # power1 = 0
        # value2 = 0
        # power2 = 0
        # while l1.next != None:
        #     value1 += l1.val * 10 ^ power1
        #     power1 += 1
        #
        # while l1.next != None:
        #     value2 += l2.val * 10 ^ power2
        #     power2 += 1
        #
        # sum = value2 + value1
        # value = sum % 10
        # head = ListNode(value, None)
        # pre_node = head
        # sum = sum // 10
        # while sum != 0:
        #     value = sum % 10
        #     tail = ListNode(value, None)
        #     sum = sum // 10
        #     pre_node.next = tail
        #     pre_node = tail
        #
        # return head


