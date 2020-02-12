import json


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return json.dumps(self._serialize(root, 0))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        _data = json.loads(data)
        return self._deserialize(_data, 0)

    @staticmethod
    def _serialize(root, c):
        if root is None:
            return []
        else:
            l = Codec._serialize(root.left, c + 1)
            r = Codec._serialize(root.right, c + 1 + len(l))
            s = (root.val, None if len(l) == 0 else c + 1, None if len(r) == 0 else c + 1 + len(l))
            return [s] + l + r

    @staticmethod
    def _deserialize(data, c):
        if not data or c is None:
            return None

        v, l, r = data[c]
        n = TreeNode(v)
        n.left = Codec._deserialize(data, l)
        n.right = Codec._deserialize(data, r)
        return n


# This kind of input is not supported by tester temporarily
if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    print(Codec().serialize(r))
