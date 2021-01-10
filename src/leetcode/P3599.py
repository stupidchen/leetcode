MOD = 10 ** 9 + 7


class FenwickTree(object):
    """
    Class of Fenwick Tree (Binary Indexed Tree), which can efficiently update elements and get prefix sum in O(log n)
    time. (See: https://en.wikipedia.org/wiki/Fenwick_tree)
    """

    def __init__(self, length):
        """
        Init a Fenwick Tree with specific length.
        :param length: The length of Fenwick Tree
        """
        self.a = [0] * length
        self.n = length

    @staticmethod
    def _last_bit(x):
        """
        Return the last binary bit of a specific number. Example: _last_bit(6) = 2 (_last_bit(110) = 10)
        :param x: a specific number
        :return: the last binary bit of x
        """
        return x ^ (x & (x - 1))

    def update(self, x, d):
        """
        Update the element on the specific position with specific difference
        :param x: the position index
        :param d: the difference
        """
        if x == 0:
            return
        t = x
        n, a = self.n, self.a
        while t < n:
            self.a[t] += d
            t += self._last_bit(t)

    def get(self, x):
        """
        Return the prefix sum of the elements before the specific position
        :param x: the position index
        :return: the prefix sum
        """
        t, r = x, 0
        a = self.a
        while t > 0:
            r += a[t]
            t -= self._last_bit(t)
        return r


class Solution:
    def createSortedArray(self, instructions):
        m = max(instructions)
        f1 = FenwickTree(m + 1)
        f2 = FenwickTree(m + 1)
        r = 0
        for i in instructions:
            k = m - i + 1
            t1, t2 = f1.get(i - 1), f2.get(k - 1)
            f1.update(i, 1)
            f2.update(k, 1)
            r = r + min(t1, t2)
        return r % MOD
