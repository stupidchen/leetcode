from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time):
        s = defaultdict(lambda: 0)
        r = 0
        for t in time:
            r += s[(60 - t % 60) % 60]
            s[t % 60] += 1
        return r


if __name__ == '__main__':
    print(Solution().numPairsDivisibleBy60([60] * 3))
    print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))
