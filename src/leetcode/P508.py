from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        c = defaultdict(lambda: 0)

        def count_sum(node):
            if node is None:
                return 0
            s = node.val + count_sum(node.left) + count_sum(node.right)
            c[s] += 1
            return s

        count_sum(root)
        m = max(c.values())
        return filter(lambda k: c[k] == m, c.keys())

