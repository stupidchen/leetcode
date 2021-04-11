# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ret = [0]

        def depth(node, d):
            if node is None:
                return d

            return max(depth(node.left, d + 1), depth(node.right, d + 1))

        def solve(node, d, dd):
            if node is None:
                return

            if node.left is None and node.right is None and d == dd:
                ret[0] += node.val
            solve(node.left, d + 1, dd)
            solve(node.right, d + 1, dd)

        solve(root, 0, depth(root, 0) - 1)
        return ret[0]
