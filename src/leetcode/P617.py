class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None and root2 is None:
            return None

        return TreeNode((root1.val if root1 is not None else 0) + (root2.val if root2 is not None else 0),
                        self.mergeTrees(root1.left if root1 is not None else None, root2.left if root2 is not None else None),
                        self.mergeTrees(root1.right if root1 is not None else None, root2.right if root2 is not None else None),
                        )
