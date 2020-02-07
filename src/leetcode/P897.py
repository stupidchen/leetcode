# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = TreeNode(-1)

    def generate(self, root):
        if not root:
            return
        self.generate(root.left)
        self.ans.right = TreeNode(root.val)
        self.ans = self.ans.right
        self.generate(root.right)

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        t = self.ans
        self.generate(root)
        return t.right
