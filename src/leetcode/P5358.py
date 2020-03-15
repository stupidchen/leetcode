# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root):
        def combine(node):
            if node is None:
                return []
            return combine(node.left) + [node.val] + combine(node.right)

        def resolve(arr, lo, hi):
            if lo > hi:
                return None

            m = (hi + lo) >> 1
            r = TreeNode(arr[m])
            r.left = resolve(arr, lo, m - 1)
            r.right = resolve(arr, m + 1, hi)
            return r

        a = combine(root)
        return resolve(a, 0, len(a) - 1)


if __name__ == '__main__':
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.right = TreeNode(3)
    r.right.right.right = TreeNode(4)
    t = Solution().balanceBST(r)
    print(t)
