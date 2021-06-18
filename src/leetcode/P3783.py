class FenwickTree(object):
    def __init__(self, length):
        self.a = [0] * length
        self.n = length

    @staticmethod
    def _last_bit(x):
        return x ^ (x & (x - 1))

    def update(self, x, d):
        if x == 0:
            return
        t = x
        n, a = self.n, self.a
        while t < n:
            self.a[t] += d
            t += self._last_bit(t)

    def get(self, x):
        t, r = x, 0
        a = self.a
        while t > 0:
            r += a[t]
            t -= self._last_bit(t)
        return r


class NumArray:

    def __init__(self, nums):
        n = len(nums)
        self.ta = FenwickTree(n + 1)
        self.a = nums
        for i in range(n):
            self.ta.update(i + 1, nums[i])

    def update(self, i: int, val: int) -> None:
        self.ta.update(i + 1, val - self.a[i])
        self.a[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.ta.get(j + 1) - self.ta.get(i)
