# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def find(node, parent, target):
    if node is None:
        return None, -1
    if node.val == target:
        return parent, 0
    elif node.left is None and node.right is None:
        return None, -1

    lp, ld = find(node.left, node, target)
    rp, rd = find(node.right, node, target)
    if lp is None and rp is None:
        return None, -1
    elif lp is not None:
        return lp, ld + 1
    else:
        return rp, rd + 1

class Solution:
    def isCousins(self, root, x, y):
        xp, xd = find(root, None, x)
        yp, yd = find(root, None, y)
        return xd == yd and xp != yp

