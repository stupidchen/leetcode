class Solution:
    def findBottomLeftValue(self, root):
        q = [root]
        while q:
            node = q.pop(0)
            if not q and not node.left and not node.right:
                return node.val
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
