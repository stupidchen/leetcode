from collections import Counter, defaultdict


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False

        p = defaultdict(lambda: [])
        d = [0] * 10
        for i, c in enumerate(s):
            p[ord(c) - 48].append(i)

        for i, c in enumerate(t):
            t = ord(c) - 48
            if d[t] >= len(p[t]):
                return False
            for j in range(t):
                if d[j] < len(p[j]) and p[j][d[j]] < p[t][d[t]]:
                    return False
            d[t] += 1

        return True


if __name__ == '__main__':
    print(Solution().isTransformable('12435', '12345'))
