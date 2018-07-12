# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, cur, path, sto):
        if cur is None:
            return
        if cur.left is None and cur.right is None:
            sto.append(path + str(cur.val))
            return

        self.solve(cur.left, path + str(cur.val) + '->', sto)
        self.solve(cur.right, path + str(cur.val) + '->', sto)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        self.solve(root, '', ret)
        return ret