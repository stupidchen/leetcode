# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from math import inf


class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        c = defaultdict(lambda: -inf)

        def find(node, depth):
            if node is None:
                return
            c[depth] = max(c[depth], node.val)
            find(node.left, depth + 1)
            find(node.right, depth + 1)
        find(root, 0)
        m = max(c.keys())
        r = []
        for i in range(m + 1):
            r.append(c[i])
        return r
