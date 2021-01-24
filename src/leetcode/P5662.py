from collections import Counter
from math import inf

LOWER = 'bcdefghijklmnopqrstuvwxyz'

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        def make_less(x, y):
            r = inf
            cx = Counter(x)
            cy = Counter(y)
            kx = sorted(cx.keys())
            ky = sorted(cy.keys())

            for c in LOWER:
                t = 0
                for i in kx:
                    if i < c:
                        t += cx[i]
                for i in ky:
                    if i >= c:
                        t += cy[i]
                r = min(r, t)

            return r

        def make_one(x):
            c = Counter(x)
            return len(x) - max(c.values())

        return min(make_less(a, b), make_less(b, a), make_one(a) + make_one(b))


if __name__ == '__main__':
    print(Solution().minCharacters("zy", "wx"))
    print(Solution().minCharacters("ace", "abe"))
    print(Solution().minCharacters("jukdyrwxmayusovrggihfiluaewjbixpxybjfsjuyjcdnsxacodbwfdbfyklwfkblnijmhwivo",
                                   "sdtinjseqrjmmumheuimgmnwfjgwftdldjwpugupnwnltslplgufmynmsovqnculunfycwlxrcregkwkvlwwkhitqyiavabxhu"))
