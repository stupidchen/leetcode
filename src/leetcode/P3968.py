class Solution:
    def shiftingLetters(self, S, shifts):
        n = len(shifts)
        if n == 0:
            return S
        f = [0] * n
        f[n - 1] = shifts[n - 1] % 26
        for i in range(n - 2, -1, -1):
            f[i] = (f[i + 1] + shifts[i]) % 26
        ret = ''
        for i in range(n):
            c = (ord(S[i]) - ord('a') + f[i]) % 26 + ord('a')
            ret += chr(c)
        return ret