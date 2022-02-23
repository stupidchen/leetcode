from collections import defaultdict
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(lambda: 0)

        def cal(node, level):
            if node is None:
                return

            d[level] += node.val
            cal(node.left, level + 1)
            cal(node.right, level + 1)

        cal(root, 1)
        m = max(d.values())
        for k, v in d.items():
            if v == m:
                return k

