# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        g = set()
        s = {}

        def calculateSum(node):
            if node is None:
                return

            calculateSum(node.right)
            s[node] = node.val + sum([n.val for n in g])
            g.add(node)
            calculateSum(node.left)

        calculateSum(root)
        if root is not None:
            q = [root]
            h = 0
            while h < len(q):
                q[h].val = s[q[h]]
                if q[h].left is not None:
                    q.append(q[h].left)
                if q[h].right is not None:
                    q.append(q[h].right)
                h += 1
        return root


if __name__ == '__main__':
    r = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    Solution().convertBST(r)
    print(r.val)
