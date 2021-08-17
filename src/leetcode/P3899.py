# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        def solve(node, m):
            if node is None:
                return 0

            r = 1 if node.val >= m else 0
            t = max(m, node.val)
            return r + solve(node.left, t) + solve(node.right, t)

        return solve(root, float('-inf'))
