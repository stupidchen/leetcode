class Solution:
    def addOneRow(self, root, v, d):
        if d == 1:
            r = TreeNode(v, root)
            return r
        else:
            def find(node, depth):
                if node is None:
                    return
                if depth == d:
                    nl = TreeNode(v, left=node.left)
                    nr = TreeNode(v, right=node.right)
                    node.left = nl
                    node.right = nr
                    return
                find(node.left, depth + 1)
                find(node.right, depth + 1)

            find(root, 2)

            return root
