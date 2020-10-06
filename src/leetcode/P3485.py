# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(node):
            if node is None:
                return
            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    insert(node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    insert(node.right)
        if root is None:
            root = TreeNode(val)
        else:
            insert(root)

        return root
