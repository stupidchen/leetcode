class Solution:
    def minSumOfLengths(self, arr, target):
        def ps(a):
            n = len(a)
            r = [-1] * n
            c = 0
            d = {0: -1}
            for i in range(len(arr)):
                c += a[i]
                if i > 0:
                    r[i] = r[i - 1]
                if c - target in d:
                    if r[i] == -1 or r[i] > i - d[c - target]:
                        r[i] = i - d[c - target]
                d[c] = i
            return r

        p = ps(arr)
        s = ps(list(reversed(arr)))
        n = len(arr)
        r = -1
        for i in range(n - 1):
            if p[i] == -1 or s[n - i - 2] == -1:
                continue
            if r == -1 or r > p[i] + s[n - i - 2]:
                r = p[i] + s[n - i - 2]
        return r


if __name__ == '__main__':
    print(Solution().minSumOfLengths([3, 1, 1, 1, 5, 1, 2, 1], 3))
