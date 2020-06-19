HMOD = (1 << 63) - 1

class Solution:
    def longestDupSubstring(self, S):
        a = [ord(c) - ord('a') for c in S]

        def solve(le):
            t = 0
            for i in range(le):
                t = (t * 26 + a[i]) % HMOD
            d = {t}
            p = pow(26, le, HMOD)
            for i in range(le, len(S)):
                t = (t * 26 - a[i - le] * p + a[i]) % HMOD
                if t in d:
                    return S[i-le+1:i+1]
                d.add(t)
            return None

        l, r = 1, len(S) - 1
        ret = ''
        while l <= r:
            mid = (l + r) >> 1
            t = solve(mid)
            if t is not None:
                ret = t
                l = mid + 1
            else:
                r = mid - 1
        return ret


if __name__ == '__main__':
    print(Solution().longestDupSubstring('banana'))
    print(Solution().longestDupSubstring('abcd'))
