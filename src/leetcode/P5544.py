class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        add_all = (b & 1 == 1) or (b & 1 == 0 and n & 1 == 1)

        def find_min(x):
            vv = set()
            r = x
            rt = 0
            for i in range(10):
                t = (i * a + x) % 10
                if r > t:
                    rt = i
                    r = t
            return r, rt

        v = set()
        r = s
        for i in range(n):
            t = (i * b) % n
            if t in v:
                break
            v.add(t)

            tt = t
            if t & 1 == 0:
                tt = (t + 1) % n
            ts = list(s)
            u = int(ts[tt])
            min_u, min_j = find_min(u)
            for i in range(n >> 1):
                ts[tt] = str((int(ts[tt]) + min_j * a) % 10)
                tt = (tt + 2) % n

            if add_all:
                tt = t
                if t & 1 == 1:
                    tt = (t + 1) % n
                u = int(ts[tt])
                min_u, min_j = find_min(u)
                for i in range(n >> 1):
                    ts[tt] = str((int(ts[tt]) + min_j * a) % 10)
                    tt = (tt + 2) % n
            ts = ''.join(ts)
            ts = ts[t:] + ts[:t]
            if ts < r:
                r = ts

        return r


if __name__ == '__main__':
    print(Solution().findLexSmallestString("5525", 9, 2))
    print(Solution().findLexSmallestString("74", 5, 1))
    print(Solution().findLexSmallestString(s = "43987654", a = 7, b = 3))
