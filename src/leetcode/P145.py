# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        s = [(root, 'L')]
        ret = []
        while len(s) != 0:
            c = s[-1][0]
            d = s[-1][1]
            if d == 'L':
                if c.left is not None:
                    s[-1] = (c, 'R')
                    s.append((c.left, 'L'))
                    continue
                d = 'R'
            if d == 'R':
                if c.right is not None:
                    s[-1] = (c, 'T')
                    s.append((c.right, 'L'))
                    continue
                d = 'T'
            if d == 'T':
                ret.append(c.val)
                s.pop()
        return ret
