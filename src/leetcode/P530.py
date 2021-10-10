# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def getMinimumDifference(self, root) -> int:
        def get_list(node):
            if node is None:
                return []
            return get_list(node.left) + [node.val] + get_list(node.right)

        a = get_list(root)
        r = abs(a[1] - a[0])
        for i in range(2, len(a)):
            r = min(r, abs(a[i] - a[i - 1]))
        return r
