# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None

        if original == target:
            return cloned
        else:
            t = self.getTargetCopy(original.left, cloned.left, target)
            if t is not None:
                return t
            else:
                return self.getTargetCopy(original.right, cloned.right, target)
