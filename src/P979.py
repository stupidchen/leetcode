# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = {
            'ret': 0
        }

        def solve(node, parent):
            if node is None:
                return

            solve(node.left, node)
            solve(node.right, node)

            if node.val <= 0:
                if parent is not None:
                    parent.val -= 1 - node.val
                    ret['ret'] += 1 - node.val
            elif node.val > 1:
                parent.val += node.val - 1
                ret['ret'] += node.val - 1
            return

        solve(root, None)

        return ret['ret']


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.left.right.left = TreeNode(0)

    print(Solution().distributeCoins(root))
