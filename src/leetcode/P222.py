# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ANS = 0

    def getDepth(self, node):
        if node is None:
            return 0
        return self.getDepth(node.left) + 1

    def subNodes(self, node, index, depth, target):
        if node is None:
            return -1

        if depth == target:
            return index

        if node.right is not None:
            if self.getDepth(node.right) + depth == target:
                return self.subNodes(node.right, index + (1 << (target - depth - 1)), depth + 1, target)

        return self.subNodes(node.left, index, depth + 1, target)

    def countNodes(self, root):
        depth = self.getDepth(root)
        self.ANS = (1 << depth) - 1
        if depth <= 1:
            return self.ANS
        t = self.subNodes(root, 0, 1, depth)
        return self.ANS - ((1 << (depth - 1)) - t - 1)


if __name__ == '__main__':
    l = TreeNode(2)
    r = TreeNode(3)
    ll = TreeNode(4)
    lr = TreeNode(5)
    rl = TreeNode(6)
    rr = TreeNode(7)
    root = TreeNode(1)
    root.left = l
    root.right = r
    l.left = ll
    l.right = rr
    print(Solution().countNodes(root))
