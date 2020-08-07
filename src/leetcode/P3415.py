# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        q = [(root, 0, 0)]
        from collections import defaultdict
        v = defaultdict(lambda: [])
        h = 0
        while h < len(q):
            v[q[h][1]].append((q[h][2], q[h][0].val))
            if q[h][0].left is not None:
                q.append((q[h][0].left, q[h][1] - 1, q[h][2] + 1))
            if q[h][0].right is not None:
                q.append((q[h][0].right, q[h][1] + 1, q[h][2] + 1))
            h += 1
        ret = [list(map(lambda p: p[1], sorted(v[col]))) for col in sorted(v.keys())]
        return ret
