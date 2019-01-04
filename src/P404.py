class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        tmp = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            tmp = root.left.val
        return tmp + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
