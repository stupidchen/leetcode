import math
import functools


class Solution:
    @functools.lru_cache(maxsize=None)
    def countDigitOne(self, n: int) -> int:
        s = Solution()
        if n < 1:
            return 0
        elif n <= 9:
            return 1
        else:
            l = math.floor(math.log10(n))
            b = 10 ** l
            r = 0
            t = s.countDigitOne(n % b)
            r += t
            f = n // b
            if f == 1:
                r += s.countDigitOne((10 ** l) - 1) + (n % b) + 1
            else:
                r += f * s.countDigitOne((10 ** l) - 1) + b
            return r


# For test only
SI = ((111,), (13,), (20,))
SO = (36, 6, 12)
TM = 'countDigitOne'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
