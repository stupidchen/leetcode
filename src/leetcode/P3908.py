from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def get(node: TreeNode, d: int):
            if node is None:
                return

            first, last = (node.left, node.right)[::d]
            yield from get(first, d)
            yield node.val
            yield from get(last, d)

        head, tail = get(root, 1), get(root, -1)
        p1, p2 = next(head), next(tail)
        while p1 < p2:
            if p1 + p2 > k:
                p2 = next(tail)
            elif p1 + p2 < k:
                p1 = next(head)
            else:
                return True
        return False
