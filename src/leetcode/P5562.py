from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        d = c.values()
        d = sorted(d, reverse=True)
        i = 1
        r = 0
        l = 0
        while i < len(d):
            if d[i] >= d[l]:
                t = d[i] - d[l] + 1
                d[i] -= t
                r += t
            if d[i] != 0:
                l = i
            i += 1
        return r


if __name__ == '__main__':
    print(Solution().minDeletions('bbcebab'))
