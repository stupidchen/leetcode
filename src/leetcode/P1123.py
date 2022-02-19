class Solution:
    ANS = None

    DEPTH = 0

    def solveDepth(self, cur, depth):
        if cur is None:
            return

        if depth > self.DEPTH:
            self.DEPTH = depth
        self.solveDepth(cur.left, depth + 1)
        self.solveDepth(cur.right, depth + 1)

    def solve(self, cur, depth):
        if cur is None:
            return depth - 1

        ll = self.solve(cur.left, depth + 1)
        rr = self.solve(cur.right, depth + 1)
        if ll == rr == self.DEPTH:
            self.ANS = cur
        return max(ll, rr)

    def lcaDeepestLeaves(self, root):
        self.ANS = root
        self.DEPTH = 0
        self.solveDepth(root, 0)
        self.solve(root, 0)
        return self.ANS
