from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(lambda: 0)
        for i in range(lowLimit, highLimit + 1):
            s = str(i)
            r = sum([int(c) for c in s])
            d[r] += 1
        return max(d.values())


if __name__ == '__main__':
    print(Solution().countBalls(1, 10))
