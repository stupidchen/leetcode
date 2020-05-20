# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    index = 0

    def num(self, node, target):
        if node is None:
            return
        t = self.num(node.left, target)
        if t is not None:
            return t
        self.index += 1
        if self.index == target:
            return node
        t = self.num(node.right, target)
        return t

    def kthSmallest(self, root, k):
        ret = self.num(root, k)
        if ret is not None:
            return ret.val
        return
