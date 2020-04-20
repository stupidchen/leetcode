# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder):
        from bisect import bisect
        if len(preorder) == 0:
            return None
        r = TreeNode(preorder[0])
        t = bisect(preorder, preorder[0], 1)
        r.left = self.bstFromPreorder(preorder[1:t])
        r.right = self.bstFromPreorder(preorder[t:])
        return r


if __name__ == '__main__':
    print(Solution().bstFromPreorder([4, 2]))
