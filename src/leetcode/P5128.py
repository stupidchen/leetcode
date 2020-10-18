import bisect


def find_prime(n):
    t = [True] * n
    t[0] = False
    t[1] = False
    r = []
    for i in range(2, n):
        if t[i]:
            j = i * i
            while j < n:
                t[j] = False
                j += i
            r.append(i)
    return r


class Solution:
    def areConnected(self, n, threshold, queries):
        primes = find_prime(n + 1)
        m = len(primes)
        fp = bisect.bisect_right(primes, threshold)
        b = [i for i in range(n)]
        s = [1] * n

        def find(x):
            if b[x] != x:
                b[x] = find(b[x])
            return b[x]

        def merge(x, y):
            bx = find(x)
            by = find(y)
            if s[bx] > s[by]:
                b[by] = b[bx]
            else:
                b[bx] = b[by]
                s[by] = max(s[bx] + 1, s[by])

        v = set()
        for i in range(threshold + 1, n + 1):
            if i not in v:
                q = [i]
                v.add(i)
                h = 0
                while h < len(q):
                    t = q[h]
                    for j in range(0, m):
                        p = primes[j]
                        tt = t * p
                        if tt <= n:
                            merge(tt - 1, i - 1)
                            if tt not in v:
                                v.add(tt)
                                q.append(tt)
                    h += 1

        r = []
        for x, y in queries:
            r.append(find(x - 1) == find(y - 1))
        return r


if __name__ == '__main__':
    print(Solution().areConnected(n=26, threshold=3, queries=[[12, 6]]))
    print(Solution().areConnected(n=6, threshold=2, queries=[[1, 4], [2, 5], [3, 6]]))
