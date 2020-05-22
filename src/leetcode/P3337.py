from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        d = [(t[1], t[0]) for t in c.items()]
        d = sorted(d, reverse=True)
        r = ''
        for f, c in d:
            r += c * f
        return r


if __name__ == '__main__':
    print(Solution().frequencySort('Aabb'))
