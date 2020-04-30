# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root, arr):
        def solve(node, a):
            if node is None:
                return len(a) == 0
            if len(a) == 0:
                return False
            if node.val != a[0]:
                return False
            t = a[1:]
            if node.left is None and node.right is None:
                return len(t) == 0
            elif node.left is not None and solve(node.left, t):
                return True
            elif node.right is not None and solve(node.right, t):
                return True
            return False

        return solve(root, arr)


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(0)
    r.right = TreeNode(1)
    print(Solution().isValidSequence(r, [1, 0]))
