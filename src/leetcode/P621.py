from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        c = dict(Counter(tasks))
        m = len(tasks)
        t = {i: float('-inf') for i in c.keys()}
        r = 0

        def next_t(x, y):
            if t[x] < 0:
                return y + 1
            return max(y + 1, t[x] + n + 1)

        for i in range(m):
            mt, mc, mk = float('inf'), 0, None
            for k in t:
                rr = next_t(k, r)
                if c[k] > 0 and ((rr < mt) or (mt == rr and c[k] > mc)):
                    mc = c[k]
                    mt = rr
                    mk = k
            r = mt
            t[mk] = r
            c[mk] -= 1
            if c[mk] == 0:
                del t[mk]
        return r


if __name__ == '__main__':
    print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
