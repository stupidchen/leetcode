# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        def solve(node):
            if node is None:
                return 0, 0, 0

            ll, lr, lp = solve(node.left)
            rl, rr, rp = solve(node.right)
            l = max(ll, lr)
            r = max(rl, rr)
            return l + 1, r + 1, max(l + r, max(lp, rp))

        return solve(root)[2]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root))
