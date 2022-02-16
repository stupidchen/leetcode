# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        ret = head
        if head.next is not None:
            ret = head.next

        while head is not None and head.next is not None:
            next_node = head.next.next
            head.next.next = head
            if next_node is not None and next_node.next is not None:
                head.next = next_node.next
            else:
                head.next = next_node
            head = next_node
        return ret
