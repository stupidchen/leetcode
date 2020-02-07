class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []

    def solve(self, c, d):
        if c is None:
            return
        if d >= len(self.ans):
            self.ans.append(c.val)
        else:
            self.ans[d] = c.val
        self.solve(c.left, d + 1)
        self.solve(c.right, d + 1)

    def rightSideView(self, root):
        self.ans = []
        self.solve(root, 0)
        return self.ans
