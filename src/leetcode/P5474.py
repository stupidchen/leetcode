# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def solve(c: TreeNode):
            if c is None:
                return 0, {}

            if c.left is None and c.right is None:
                return 0, {0: [id(c)]}

            lt, ld = solve(c.left)
            rt, rd = solve(c.right)
            r = lt + rt
            for lk, lv in ld.items():
                if lk + 1 < distance:
                    for rk, rv in rd.items():
                        if lk + rk + 2 <= distance:
                            r += len(rv) * len(lv)

            rtd = {}
            for rk, rv in rd.items():
                rtd[rk + 1] = rv
            for lk, lv in ld.items():
                if lk + 1 not in rtd:
                    rtd[lk + 1] = lv
                else:
                    rtd[lk + 1].extend(lv)

            return r, rtd

        return solve(root)[0]


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(2)
    # r.left.right = TreeNode(2)
    r.right = TreeNode(3)
    #r.right.left = TreeNode(2)
    # r.right.right = TreeNode(2)
    print(Solution().countPairs(r, 3))
