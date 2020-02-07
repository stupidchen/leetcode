# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def count(node):
    if not node:
        return 0
    return count(node.left) + count(node.right) + 1

class CBTInserter:

    def __init_sib__(self, node, index):
        if not node:
            return
        self.data[index] = node.val
        self.__init_sib__(node.left, index << 1)
        self.__init_sib__(node.right, (index << 1) + 1)

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = [0] * (count(root) + 1)
        self.root = None
        self.__init_sib__(root, 1)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        self.data.append(v)
        self.root = None
        return self.data[(len(self.data) - 1) >> 1]

    def rebuild(self, index):
        if len(self.data) > index:
            ret = TreeNode(self.data[index])
            ret.left, ret.right = self.rebuild(index << 1), self.rebuild((index << 1) + 1)
            return ret
        return None

    def get_root(self):
        """
        :rtype: TreeNode
        """
        if not self.root:
            self.root = self.rebuild(1)
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()

if __name__ == '__main__':
    root = TreeNode(1)
    l = TreeNode(2)
    r = TreeNode(3)
    ll = TreeNode(4)
    lr = TreeNode(5)
    rl = TreeNode(6)
    l.left = ll
    l.right = lr
    r.left = rl
    root.left = l
    root.right = r
    obj = CBTInserter(root)
    print(obj.insert(7))
    print(obj.insert(8))
    print(obj.get_root())
