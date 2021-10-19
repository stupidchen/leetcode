from typing import Optional

from src.leetcode.P1305 import TreeNode


def eq(node, other):
    if node is None and other is None:
        return True
    if node is None or other is None:
        return False
    if node.val != other.val:
        return False
    return eq(node.left, other.left) and eq(node.right, other.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        return eq(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
