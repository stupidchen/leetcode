# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        return self._remove(root, key)

    def _remove(self, node, value):
        if node is None:
            return None

        if node.val == value:
            if node.left is not None:
                node = self._zag(node)
                node.right = self._remove(node.right, value)
            else:
                node = node.right
        else:
            if node.val < value:
                node.right = self._remove(node.right, value)
            else:
                node.left = self._remove(node.left, value)
        return node

    @staticmethod
    def _zag(node):
        c = node
        a = node.left
        c.left = a.right
        a.right = c
        return a
