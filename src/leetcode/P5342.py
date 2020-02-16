class Solution:
    def maxEvents(self, events):
        if not events:
            return 0
        events = sorted(events, key=lambda e: (e[1], e[0]))
        n = 0
        for e in events:
            n = max(e[1], n)
        f = []
        a = []
        n += 1
        for i in range(n):
            f.append(i)
            a.append(False)

        r = 0
        for e in events:
            c = e[0]
            while c < n and a[c]:
                c = f[c]
            if c <= e[1] and not a[c]:
                r += 1
                a[c] = True
                f[c] = f[c] + 1
                t = c
                while t < n and a[t]:
                    t = f[t]
                if t < n and not a[t]:
                    f[c] = t
                else:
                    f[c] = n
        return r


# For test only
SI = (([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]],),
      ([[1, 2], [2, 3], [3, 4]],),
      ([[1, 2], [2, 3], [3, 4], [1, 2]],),
      ([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]],),
      ([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],))
SO = (5, 3, 4, 4, 7)
TM = 'maxEvents'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
