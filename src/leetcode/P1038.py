class Solution:
    def bstToGst(self, root):
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
