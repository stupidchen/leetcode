# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if root is None:
            return ''

        def convert(x):
            return chr(x + ord('a'))

        q = [(root, convert(root.val))]
        h = 0
        ret = None
        while h < len(q):
            if q[h][0].left is None and q[h][0].right is None:
                if ret is None or ret > q[h][1]:
                    ret = q[h][1]
            else:
                if q[h][0].left is not None:
                    q.append((q[h][0].left, convert(q[h][0].left.val) + q[h][1]))
                if q[h][0].right is not None:
                    q.append((q[h][0].right, convert(q[h][0].right.val) + q[h][1]))

            h += 1

        return ret
