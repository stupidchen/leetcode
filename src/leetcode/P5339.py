# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def solve(node: TreeNode):
            if node is None:
                return float('-inf'), 0, float('inf'), float('-inf'), True
            l, r = solve(node.left), solve(node.right)
            tl, sl, minl, maxl, bl = l
            tr, sr, minr, maxr, br = r

            s = sl + sr + node.val
            t = max(tl, tr)
            b = False
            if maxl < node.val < minr and bl and br:
                t = max(t, s)
                b = True
            minv = min(minl, minr, node.val)
            maxv = max(maxl, maxr, node.val)
            return t, s, minv, maxv, b

        return max(solve(root)[0], 0)


if __name__ == '__main__':
    r = TreeNode(-4)
    r.left = TreeNode(-2)
    r.right = TreeNode(-5)
    print(Solution().maxSumBST(r))
