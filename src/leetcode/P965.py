# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        d = {}

        def solve(node):
            if node is None:
                return
            d[node.val] = True
            solve(node.left)
            solve(node.right)

        solve(root)
        return len(d.keys()) == 1


if __name__ == '__main__':
    node = TreeNode(5)
    node.left = TreeNode(5)
    node.right = TreeNode(3)
    print(Solution().isUnivalTree(node))
