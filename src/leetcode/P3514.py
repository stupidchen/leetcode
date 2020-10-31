# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from math import inf
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = [None, None]
        prev = [TreeNode(-inf)]

        def find(node):
            if node is None:
                return

            find(node.left)
            if node.val <= prev[0].val and nodes[0] is None:
                nodes[0] = prev[0]
            if node.val <= prev[0].val and nodes[0] is not None:
                nodes[1] = node
            prev[0] = node

            find(node.right)

        find(root)
        t = nodes[0].val
        nodes[0].val = nodes[1].val
        nodes[1].val = t
