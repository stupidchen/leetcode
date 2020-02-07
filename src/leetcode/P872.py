class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getLeafs(self, c, s):
        if c.left is None and c.right is None:
            s.append(c.val)
            return
        if c.left is not None:
            self.getLeafs(c.left, s)
        if c.right is not None:
            self.getLeafs(c.right, s)

    def leafSimilar(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        l1 = []
        l2 = []
        self.getLeafs(root1, l1)
        self.getLeafs(root2, l2)
        if len(l1) != len(l2):
            return False
        for (e1, e2) in zip(l1, l2):
            if e1 != e2:
                return False
        return True
