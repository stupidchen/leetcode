# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


C = 0

from collections import defaultdict


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def mark(node):
            if node is None:
                return
            global C
            C += 1
            node.n = C
            mark(node.left)
            mark(node.right)

        mark(root)

        f = defaultdict(lambda: [-1, -1])

        def solve(node, d):
            if node is None:
                return 0

            if f[node.n][d] != -1:
                return f[node.n][d]

            solve(node.left, 0)
            solve(node.left, 1)
            solve(node.right, 0)
            solve(node.right, 1)
            if d == 0:
                f[node.n][d] = solve(node.right, 1) + 1
            else:
                f[node.n][d] = solve(node.left, 0) + 1

            return f[node.n][d]

        solve(root, 0)
        solve(root, 1)
        r = 0
        for i in f:
            r = max(max(f[i]), r)
        return r - 1


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(1)
    r.left.left = TreeNode(1)
    r.right = TreeNode(1)
    r.right.left = TreeNode(1)
    r.right.left.left = TreeNode(1)
    r.right.left.left.right = TreeNode(1)
    r.right.right = TreeNode(1)
    r.right.right.left = TreeNode(1)
    r.right.right.left.right = TreeNode(1)
    print(Solution().longestZigZag(r))
