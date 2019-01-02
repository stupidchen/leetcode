# Definition for a binary tree node.
from functools import lru_cache

INF = 0xffffffff


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        @lru_cache(maxsize=None)
        def solve(node, t):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                if t == 1:
                    return INF
                if t == 0:
                    return 1
                if t == -1:
                    return 0

            l = []
            for i in range(3):
                l.append(solve(node.left, i - 1))
            r = []
            for i in range(3):
                r.append(solve(node.right, i - 1))

            if t == -1:
                if node.left is not None and node.right is not None:
                    return min(min(l[2], l[1]) + min(r[2], r[1]), min(r[2], r[1]) + min(l[2], l[1]))
                if node.left is not None:
                    return min(l[2], l[1])
                else:
                    return min(r[2], r[1])
            if t == 0:
                return 1 + min(l) + min(r)
            if t == 1:
                if node.left is not None and node.right is not None:
                    return min(l[1] + min(r[2], r[1]), r[1] + min(l[2], l[1]))
                if node.left is not None:
                    return l[1]
                else:
                    return r[1]

        return min(solve(root, 0), solve(root, 1))


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.left.left = TreeNode(4)
    node.left.left.left.left = TreeNode(5)
    node.left.left.left.left.left = TreeNode(6)
    print(Solution().minCameraCover(node))
