MOD = 10 ** 9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        r, t = 1, n
        for i in range(2, n * 2 + 1):
            j = i
            while (j & 1) == 0 and t > 0:
                j = j >> 1
                t -= 1
            r = (r * j) % MOD
        return r


# For test only
SI = ((2,), (3,))
SO = (6, 90)
TM = 'countOrders'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
