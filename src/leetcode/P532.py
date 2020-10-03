from collections import defaultdict


class Solution:
    def findPairs(self, nums, k):
        d = defaultdict(lambda: 0)
        for num in nums:
            d[num] += 1

        r = 0
        for num in d:
            if k != 0:
                if num + k in d:
                    r += 1
            else:
                if d[num] > 1:
                    r += 1
        return r


if __name__ == '__main__':
    print(Solution().findPairs([3, 1, 4, 3, 5], 2))
