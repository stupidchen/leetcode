import heapq

import random


class TreapNode(object):
    """
    Node class of Treap. It consist of four part: value, count, rank and references of sons.
    """

    def __init__(self, value):
        """
        Init a node of Treap.
        :param value: value that node holds
        """
        self.v = value
        self.c = 1
        self.ra = random.random()
        self.l, self.r = None, None


class Treap(object):
    """
    Class of Treap, which is binary search tree data structures that maintain a dynamic set of ordered keys and allow
    binary searches among the keys. (See: https://en.wikipedia.org/wiki/Treap)
    """

    def __init__(self):
        """
        Init a Treap.
        """
        self.root = None

    #   a           c
    #  / \         / \
    # b   c  -->  a   e
    #    / \     / \
    #   d   e   b   d
    @staticmethod
    def _zig(node):
        """
        Zig rotation (Left rotation) of the binary tree. The example diagram is on the above.
        (See: http://www.btechsmartclass.com/data_structures/splay-trees.html)
        :param node: The top node which the rotation happen on.
        :return: the top node after the rotation happened.
        """
        a = node
        c = node.r
        a.r = c.l
        c.l = a
        return c

    #     c           a
    #    / \         / \
    #   a   e  -->  b   c
    #  / \             / \
    # b   d           d   e
    @staticmethod
    def _zag(node):
        """
        Zag rotation (Right rotation) of the binary tree. The example diagram is on the above.
        (See: http://www.btechsmartclass.com/data_structures/splay-trees.html)
        :param node: The top node which the rotation happen on.
        :return: the top node after the rotation happened.
        """
        c = node
        a = node.l
        c.l = a.r
        a.r = c
        return a

    def add(self, value):
        """
        Add a node with specific value into the Treap.
        :param value: value of the new node.
        :return: None
        """
        self.root = self._add(self.root, value)

    def _add(self, node, value):
        """
        Add a node with specific value into the subtree which the root is the specific node.
        :param node: the root node of the subtree.
        :param value: value of the new node.
        :return: the root node of the new subtree.
        """
        if node is None:
            return TreapNode(value)

        if node.v == value:
            node.c += 1
        else:
            if node.v < value:
                node.r = self._add(node.r, value)
                if node.r.ra < node.ra:
                    node = self._zig(node)
            else:
                node.l = self._add(node.l, value)
                if node.l.ra < node.ra:
                    node = self._zag(node)
        return node

    def remove(self, value):
        """
        Remove a node with specific value from the Treap.
        :param value: value of the removed node.
        :return: None
        """
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        """
        Remove a node with specific value from the subtree which the root is the specific node.
        :param node: the root node of the subtree.
        :param value: value of the removed node.
        :return: the root node of the removed subtree.
        """
        if node is None:
            return None

        if node.v == value:
            if node.c > 1:
                node.c -= 1
            else:
                if node.l is not None:
                    node = self._zag(node)
                    node.r = self._remove(node.r, value)
                else:
                    node = node.r
        else:
            if node.v < value:
                node.r = self._remove(node.r, value)
            else:
                node.l = self._remove(node.l, value)
        return node

    def find(self, value):
        """
        Find a node with specific value from the Treap.
        :param value: value of the node.
        :return: None if the node is not exist else return the node.
        """
        return self._find(self.root, value)

    @staticmethod
    def _find(node, value):
        """
        Find a node with specific value from the subtree which the root is the specific node.
        :param node: the root node of the subtree.
        :param value: value of the node.
        :return: None if the node is not exist else return the node.
        """
        while node and node.v != value:
            if node.v < value:
                node = node.r
            else:
                node = node.l
        return node

    def max(self):
        """
        Find the node with maximum value from the Treap.
        :return: None if the Treap is empty else return the node with maximum value.
        """
        return self._max(self.root)

    @staticmethod
    def _max(node):
        """
        Find the node with maximum value from the subtree which root is the specific node.
        :param node: the root node of the subtree.
        :return: None if the subtree is empty else return the node with maximum value.
        """
        while node and node.r is not None:
            node = node.r
        return node

    def min(self):
        """
        Return the node with minimum value from the Treap.
        :return: None if the Treap is empty else return the node with minimum value.
        """
        return self._min(self.root)

    @staticmethod
    def _min(node):
        """
        Find the node with minimum value from the subtree which root is the specific node.
        :param node: the root node of the subtree.
        :return: None if the subtree is empty else return the node with minimum value.
        """
        while node and node.l is not None:
            node = node.l
        return node

    def pred(self, node):
        """
        Find the predecessor of the specific node.
        :param node: the specific node.
        :return: None if the predecessor is not exist else return the predecessor node.
        """
        if node.l is not None:
            return self._max(node.l)
        else:
            s = self._finds(node)

            while s and s[-1].r is not node:
                node = s.pop()

            if s:
                return s[-1]
            else:
                return None

    def succ(self, node):
        """
        Find the successor of the specific node.
        :param node: the specific node.
        :return: None if the successor is not exist else return the successor node.
        """
        if node.r is not None:
            return self._min(node.r)
        else:
            s = self._finds(node)

            while s and s[-1].l is not node:
                node = s.pop()

            if s:
                return s[-1]
            else:
                return None

    def _finds(self, node):
        """
        Find the retrieve path of the specific node.
        :param node: the specifc node.
        :return: The retrieve path during the search of binary tree.
        """
        s = []
        c = self.root
        while c is not node:
            s.append(c)
            if c.v > node.v:
                c = c.l
            else:
                c = c.r
        return s


class Solution:
    def findMaxValueOfEquation(self, points, k: int):
        h = []
        r = float('-inf')
        treap = Treap()
        for point in points:
            x, y = point
            while h:
                t = h[0]
                if x - t[0] > k:
                    treap.remove(h[0][1] - h[0][0])
                    heapq.heappop(h)
                else:
                    break
            if h:
                r = max(r, x + y + treap.max().v)
            heapq.heappush(h, (x, y))
            treap.add(y - x)
        return r


if __name__ == '__main__':
    print(Solution().findMaxValueOfEquation(
        [[-19, -12], [-13, -18], [-12, 18], [-11, -8], [-8, 2], [-7, 12], [-5, 16], [-3, 9], [1, -7], [5, -4], [6, -20],
         [10, 4], [16, 4], [19, -9], [20, 19]], 6))
