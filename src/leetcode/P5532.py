# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def isEvenOddTree(self, root):
        val = defaultdict(lambda: [])

        def retreive(node, depth):
            if node is None:
                return

            val[depth].append(node.val)
            retreive(node.left, depth + 1)
            retreive(node.right, depth + 1)

        retreive(root, 0)

        for depth, values in val.items():
            if depth & 1 == 0:
                for value in values:
                    if value & 1 != 1:
                        return False
                for i in range(1, len(values)):
                    if values[i] <= values[i - 1]:
                        return False
            else:
                for value in values:
                    if value & 1 != 0:
                        return False
                for i in range(1, len(values)):
                    if values[i] >= values[i - 1]:
                        return False
        return True
