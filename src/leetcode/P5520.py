class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        r = [0]

        def solve(d, i):
            t = len(d)
            if t + n - i <= r[0]:
                return
            if i == n:
                if t > r[0]:
                    r[0] = t
                return

            for m in range(i, n):
                ts = s[i: m + 1]
                if ts not in d:
                    d.add(ts)
                    solve(d, m + 1)
                    d.remove(ts)

        solve(set(), 0)
        return r[0]


if __name__ == '__main__':
    print(Solution().maxUniqueSplit('abaabababaababcd'))
