from collections import Counter
from functools import reduce


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        s = reduce(lambda x, y: x ^ y, nums)
        t = s
        for i in range(n):
            t ^= i + 1

        c = Counter(nums)
        for i in range(n):
            if c[i + 1] == 0:
                return [t ^ (i + 1), i + 1]


if __name__ == '__main__':
    print(Solution().findErrorNums([1, 1]))
