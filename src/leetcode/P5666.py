import bisect


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        r = [0]
        rr = [n - 1]

        c = {}

        def p(x, y):
            l, r = x, y
            ret = True
            while l < r:
                if (l, r) in c:
                    ret = c[(l, r)]
                    break
                if s[l] != s[r]:
                    ret = False
                    break
                l += 1
                r -= 1
            while l > x:
                l -= 1
                r += 1
                c[(l, r)] = ret

            return ret

        for i in range(1, n):
            if p(0, i):
                r.append(i)
        for i in reversed(range(n - 1)):
            if p(i, n - 1):
                rr.append(i)

        rr = list(reversed(rr))
        m = len(rr)
        for i, v in enumerate(r):
            t = bisect.bisect_right(rr, v)
            for j in range(t, m):
                u = rr[j]
                if v + 1 <= u - 1:
                    if p(v + 1, u - 1):
                        return True
        return False


if __name__ == '__main__':
    print(Solution().checkPartitioning(s="aaaa" * 250))
