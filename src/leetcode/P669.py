class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, root.val)
            root.right = self.trimBST(root.right, root.val, high)
            return root
        if low > root.val:
            return self.trimBST(root.right, low, high)
        else:
            return self.trimBST(root.left, low, high)
