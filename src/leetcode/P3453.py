# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        r = [0]

        def solve(c, v):
            if c is None:
                return

            v = (v << 1) + c.val
            if c.left is None and c.right is None:
                r[0] += v

            solve(c.left, v)
            solve(c.right, v)

        solve(root, 0)
        return r[0]
