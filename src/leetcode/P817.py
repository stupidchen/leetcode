# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List

from src.leetcode.P142 import ListNode


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        node = head
        f = []
        while node is not None:
            f.append(node.val in nums_set)
            node = node.next

        r = 0
        f.append(False)
        for i in range(len(f)):
            if f[i] and not f[i + 1]:
                r += 1
        return r

