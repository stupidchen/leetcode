# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def prepare_list(node: ListNode):
            r = []
            while node is not None:
                r.append(node.val)
                node = node.next
            return r

        l = prepare_list(head)
        n = len(l)

        def solve(node: TreeNode):
            if node is None:
                r = [0] * (n + 1)
                r[n] = True
                return r

            tl, tr = solve(node.left), solve(node.right)
            for i in range(n + 1):
                tl[i] = tl[i] or tr[i]

            if tl[0]:
                return tl
            for i in range(n):
                if l[i] == node.val and tl[i + 1]:
                    tl[i] = True
                else:
                    tl[i] = False

            return tl

        r = solve(root)
        return r[0]
