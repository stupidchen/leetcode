# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return '()'

        return '{}({},{})'.format(root.val, self.serialize(root.left), self.serialize(root.right))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '()':
            return None

        l = 0
        for i in range(len(data)):
            c = data[i]
            if c == '(':
                l += 1
            if c == ')':
                l -= 1
            if c == ',' and l == 1:
                s = data.find('(')
                r = TreeNode(int(data[:s]))
                r.left = self.deserialize(data[s+1:i])
                r.right = self.deserialize(data[i+1:-1])
                return r

        return None


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(root)
    ans = deser.deserialize(tree)
    print(ans)
