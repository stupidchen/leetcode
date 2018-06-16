# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        t = root
        s = []
        d = []
        while t is not None:
            s.append(t)
            d.append(-1)
            tmp = t.left
            t.left = None
            t = tmp
        self.stack = s
        self.direction = d
        self.last = None

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.last is not None:
            return True
        tmp = self.next()
        self.last = tmp
        if tmp is None:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        if self.last is not None:
            tmp = self.last
            self.last = None
            return tmp
        if len(self.stack) == 0:
            return None
        if self.direction[-1] == -1:
            has_left = False
            while self.stack[-1].left is not None:
                self.stack.append(self.stack[-1].left)
                self.stack[-1].left = None
                self.direction.append(-1)
                has_left = True
            if has_left:
                self.direction[-1] = 1
                return self.stack[-1].val
            else:
                self.direction[-1] = 0
        if self.direction[-1] == 0:
            self.direction[-1] = 1
            return self.stack[-1].val
        if self.direction[-1] == 1:
            has_right = False
            if self.direction[-1] == 1 and self.stack[-1].right is not None:
                t = self.stack[-1].right
                self.direction.append(-1)
                self.stack.append(t)
                while t.left is not None:
                    self.stack.append(t.left)
                    self.direction.append(-1)
                    tmp = t.left
                    t.left = None
                    t = tmp
                has_right = True
            if has_right:
                self.direction[-1] = 1
                return self.stack[-1].val
            else:
                self.direction[-1] = 2
        while self.direction[-1] == 2:
            self.stack = self.stack[:-1]
            self.direction = self.direction[:-1]
            if len(self.stack) == 0:
                return None
            if self.direction[-1] == -1:
                self.direction[-1] = 1
            else:
                self.direction[-1] = 2
        return self.stack[-1].val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(8)
    root.right.right = TreeNode(9)
    b, v = BSTIterator(root), []
    while b.hasNext():
        v.append(b.next())
    print(v)
