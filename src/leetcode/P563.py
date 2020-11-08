# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def solve(node):
            if node is None:
                return 0, 0

            vl, rl = solve(node.left)
            vr, rr = solve(node.right)
            return abs(rl - rr) + vl + vr, rl + rr + node.val

        return solve(root)[0]


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().findTilt(root))
