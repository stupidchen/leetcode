class Solution:
    def tree2str(self, root) -> str:
        if root is None:
            return ''
        if root.left is None and root.right is None:
            return str(root.val)
        if root.left is None:
            return f'{root.val}()({self.tree2str(root.right)})'
        if root.right is None:
            return f'{root.val}({self.tree2str(root.left)})'
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'
