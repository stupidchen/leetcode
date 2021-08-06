class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        from collections import defaultdict
        ret = defaultdict(lambda: [])
        if root is None:
            return []
        q = [(root, 0)]
        h = 0
        while h < len(q):
            ret[q[h][1]].append(q[h][0].val)
            for c in q[h][0].children:
                q.append((c, q[h][1] + 1))
            h += 1
        return [ret[level] for level in range(max(ret.keys()) + 1)]
