import random


class TreapNode(object):
    def __init__(self, value):
        self.v = value
        self.c = 1
        self.ra = random.random()
        self.l, self.r = None, None


class Treap(object):
    def __init__(self):
        self.root = None

    #   a           c
    #  / \         / \
    # b   c  -->  a   e
    #    / \     / \
    #   d   e   b   d
    @staticmethod
    def _zip(node):
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
    def _zap(node):
        c = node
        a = node.l
        c.l = a.r
        a.r = c
        return a

    def add(self, value):
        self.root = self._add(self.root, value)

    def _add(self, node, value):
        if node is None:
            return TreapNode(value)

        if node.v == value:
            node.c += 1
        else:
            if node.v < value:
                node.r = self._add(node.r, value)
                if node.r.ra < node.ra:
                    node = self._zip(node)
            else:
                node.l = self._add(node.l, value)
                if node.l.ra < node.ra:
                    node = self._zap(node)
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return None

        if node.v == value:
            if node.c > 1:
                node.c -= 1
            else:
                if node.l is not None:
                    node = self._zap(node)
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
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return None

        if node.v == value:
            return node

        if node.v < value:
            return self._find(node.r, value)
        else:
            return self._find(node.l, value)

    def max(self):
        return self._max(self.root)

    @staticmethod
    def _max(node):
        while node.r is not None:
            node = node.r
        return node

    def min(self):
        return self._min(self.root)

    @staticmethod
    def _min(node):
        while node.l is not None:
            node = node.l
        return node

    def pred(self, node):
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
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        n = len(nums)
        treap = Treap()
        for i in range(n):
            if i - k - 1 >= 0:
                treap.remove(nums[i - k - 1])
            treap.add(nums[i])
            m = treap.find(nums[i])
            if m.c > 1:
                return True
            p, s = treap.pred(m), treap.succ(m)
            if p is not None:
                if abs(p.v - m.v) <= t:
                    return True
            if s is not None:
                if abs(s.v - m.v) <= t:
                    return True

        return False


# For test only
SI = (([4, 1, 6, 3], 100, 1), ([1, 2, 3, 1], 3, 0), ([1, 0, 1, 1], 1, 2), ([1, 5, 9, 1, 5, 9], 2, 3))
SO = (True, True, True, False)
TM = 'containsNearbyAlmostDuplicate'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
