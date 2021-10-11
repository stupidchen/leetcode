class Solution:
    d = 0

    def diameterOfBinaryTree(self, root) -> int:
        def height(node):
            if node is None:
                return 0
            lh, rh = height(node.left), height(node.right)
            self.d = max(self.d, (lh + rh))
            return max(lh, rh) + 1
        _ = height(root)
        return self.d
