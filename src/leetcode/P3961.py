# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        def f(l, r):
            if l >= r:
                return [None]

            ret = []
            for i in range(l, r):
                fl, fr = f(l, i), f(i + 1, r)
                for ffl in fl:
                    for ffr in fr:
                        t = TreeNode(i + 1, ffl, ffr)
                        ret.append(t)
            return ret

        return f(0, n)


if __name__ == '__main__':
    print(Solution().generateTrees(3))
