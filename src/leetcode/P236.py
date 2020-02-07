# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findNode(root, node):
    if root is None:
        return None

    if root.val == node:
        return [root.val]

    pl, pr = findNode(root.left, node), findNode(root.right, node)

    if pl is not None:
        return [root.val] + pl
    elif pr is not None:
        return [root.val] + pr
    else:
        return None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pp, pq = findNode(root, p.val), findNode(root, q.val)
        ret = None
        i = 0
        while i < len(pp) and i < len(pq):
            if pp[i] == pq[i]:
                ret = pp[i]
            else:
                break
            i += 1
        return TreeNode(ret)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left, root.right = TreeNode(5), TreeNode(1)
    root.left.left, root.left.right = TreeNode(6), TreeNode(2)
    root.right.left, root.right.right = TreeNode(0), TreeNode(8)
    root.left.right.left, root.left.right.right = TreeNode(7), TreeNode(4)
    print(Solution().lowestCommonAncestor(root, 5, 1))