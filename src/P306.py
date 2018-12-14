from functools import lru_cache


class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        @lru_cache(None)
        def valid(l, r):
            t = num[l: r]
            if t[0] == '0' and r - l > 1:
                return False
            return True

        @lru_cache(None)
        def f(x, y, z, w):
            if w == 0:
                return valid(w, z) and valid(z, y) and valid(y, x) and \
                       (int(num[w: z]) + int(num[z: y]) == int(num[y: x]))

            if valid(w, z) and valid(z, y) and valid(y, x) and \
                       (int(num[w: z]) + int(num[z: y]) == int(num[y: x])):
                for i in reversed(range(w)):
                    if f(y, z, w, i):
                        return True
                return False
            else:
                return False

        n = len(num)
        for i in reversed(range(n)):
            for j in reversed(range(i)):
                for k in reversed(range(j)):
                    if f(n, i, j, k):
                        return True
        return False

if __name__ == '__main__':
    print(Solution().isAdditiveNumber('12315'))
