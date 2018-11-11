# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        ret = 0
        if R > root.val:
            ret += self.rangeSumBST(root.right, L, R)
        if L < root.val:
            ret += self.rangeSumBST(root.left, L, R)
        if L <= root.val <= R:
            ret += root.val
        return ret
