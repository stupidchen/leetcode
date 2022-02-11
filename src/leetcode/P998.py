from typing import Optional

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            return TreeNode(val, left=root)

        root.right = self.insertIntoMaxTree(root.right, val)
        return root
