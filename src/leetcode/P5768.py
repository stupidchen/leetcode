import bisect
from itertools import accumulate


class Solution:
    def chalkReplacer(self, chalk, k):
        s = list(accumulate(chalk))
        k = k % s[-1]
        return bisect.bisect_right(s, k)


if __name__ == '__main__':
    print(Solution().chalkReplacer([5, 1, 5], 22))
    print(Solution().chalkReplacer([1, 1], 1))
