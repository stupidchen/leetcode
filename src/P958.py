# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def solve(node):
            if node is None:
                return 0, 0, True
            if node.left is None and node.right is None:
                return 1, 1, True

            depth_l, num_l, c_l = solve(node.left)
            depth_r, num_r, c_r = solve(node.right)

            if depth_l - depth_r > 1 or depth_r > depth_l or not c_l or not c_r:
                return -1, -1, False

            if depth_l == depth_r and num_l != (1 << depth_l) - 1:
                return -1, -1, False

            if depth_l > depth_r and num_r != (1 << depth_r) - 1:
                return -1, -1, False

            return max(depth_l, depth_r) + 1, num_l + num_r + 1, True

        _, _, ret = solve(root)
        return ret


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)

    print(Solution().isCompleteTree(root))
