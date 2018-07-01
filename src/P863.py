class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def solveSubTree(self, cur, k):
        if cur is None or k < 0:
            return

        if k == 0:
            self.ans.append(cur.val)
        else:
            self.solveSubTree(cur.left, k - 1)
            self.solveSubTree(cur.right, k - 1)

    def solve(self, cur, target, k):
        if cur is None:
            return -1

        if cur is target:
            self.solveSubTree(cur, k)
            return 0
        else:
            ll = self.solve(cur.left, target, k)
            rr = self.solve(cur.right, target, k)
            if ll != -1:
                ll += 1
                if ll == k:
                    self.ans.append(cur.val)
                self.solveSubTree(cur.right, k - ll - 1)
                return ll
            if rr != -1:
                rr += 1
                if rr == k:
                    self.ans.append(cur.val)
                self.solveSubTree(cur.left, k - rr - 1)
                return rr
            return -1

    def distanceK(self, root, target, K):
        self.ans = []
        self.solve(root, target, K)
        return self.ans
