class Solution:
    def fairCandySwap(self, A, B):
        cb = {}
        sa = 0
        sb = 0
        for a in A:
            sa += a
        for b in B:
            sb += b
            cb[b] = True
        d = (sb - sa) >> 1
        for a in A:
            if (a + d) in cb:
                return [a, a + d]
        return []