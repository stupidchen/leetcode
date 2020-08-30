from functools import lru_cache


class TreeNode(object):
    def __init__(self, v):
        self.l = self.r = None
        self.c = 1
        self.v = v


MOD = 10 ** 9 + 7


@lru_cache(maxsize=None)
def f(l, r):
    if l == 0 or r == 0:
        return 1
    return (f(l - 1, r) + f(l, r - 1)) % MOD


class Solution:
    def numOfWays(self, nums):
        root = TreeNode(nums[0])
        for num in nums[1:]:
            t = root
            while True:
                t.c += 1
                if num > t.v:
                    if t.r is None:
                        t.r = TreeNode(num)
                        break
                    else:
                        t = t.r
                else:
                    if t.l is None:
                        t.l = TreeNode(num)
                        break
                    else:
                        t = t.l

        def solve(c):
            if c is None:
                return 1
            cl = c.l.c if c.l is not None else 0
            cr = c.r.c if c.r is not None else 0
            return (solve(c.l) * solve(c.r) * f(cl, cr)) % MOD

        return (solve(root) - 1) % MOD


if __name__ == '__main__':
    print(Solution().numOfWays([2, 1, 3]))
