# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        d = {}

        def clone(x):
            if x.val in d:
                return d[x.val]

            t = Node(x.val)
            d[x.val] = t
            for n in x.neighbors:
                t.neighbors.append(clone(n))
            return t

        return clone(node)
