# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        if N == 1:
            return [TreeNode(0)]

        if N & 1 == 0:
            return []

        ret = []
        i = 1
        while i < N:
            ls = self.allPossibleFBT(i)
            rs = self.allPossibleFBT(N - i - 1)
            for lson in ls:
                for rson in rs:
                    node = TreeNode(0)
                    node.left = lson
                    node.right = rson
                    ret.append(node)
            i += 2
        return ret