# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def solve(node, min_val, max_val):
            if node is None:
                return 0
            r = 0
            v = node.val
            if min_val is not None:
                r = max(abs(min_val - v), r)
            if max_val is not None:
                r = max(abs(max_val - v), r)
            min_val = min(min_val, v) if min_val is not None else v
            max_val = max(max_val, v) if max_val is not None else v
            r = max(r, solve(node.left, min_val, max_val))
            r = max(r, solve(node.right, min_val, max_val))
            return r

        return solve(root, None, None)
