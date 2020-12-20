class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        m = 0
        for i, c in enumerate(S):
            if c.isdigit():
                t = int(c)
                if t * m < K:
                    m = t * m
                else:
                    return self.decodeAtIndex(S[:i], m if K % m == 0 else K % m)
            else:
                m += 1
                if m == K:
                    return c

        return ''
