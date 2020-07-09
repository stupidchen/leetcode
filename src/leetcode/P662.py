# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode):
        min_width = defaultdict(lambda: float('inf'))
        max_width = defaultdict(lambda: 0)

        def solve(level, current, number):
            if current is None:
                return

            min_width[level] = min(min_width[level], number)
            max_width[level] = max(max_width[level], number)

            solve(level + 1, current.left, number << 1)
            solve(level + 1, current.right, (number << 1) + 1)

        solve(0, root, 0)
        return max([max_width[i] - min_width[i] + 1 for i in min_width.keys()])
