class Solution:
    def decrypt(self, code, k):
        n = len(code)
        r = []
        for i in range(n):
            t = 0
            p = i
            for j in range(abs(k)):
                if k > 0:
                    p = (p + 1) % n
                else:
                    p = (p - 1) % n
                t += code[p]
            r.append(t)
        return r
