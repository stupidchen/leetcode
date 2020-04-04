from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        p = [0] * (n + 1)
        for i in range(1, n + 1):
            t = 0
            x = i
            while x > 0:
                t += x % 10
                x //= 10
            p[i] = t

        d = Counter(p[1:])
        r = 0
        m = max(d.values())
        for i in d.values():
            if i == m:
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().countLargestGroup(24))
