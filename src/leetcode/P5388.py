class Solution:
    def reformat(self, s: str) -> str:
        a, d = '', ''
        for c in s:
            if c.isdigit():
                d += c
            else:
                a += c
        if abs(len(a) - len(d)) > 1:
            return ''
        if len(a) > len(d):
            r = ''
            for i in range(len(d)):
                r += a[i] + d[i]
            r += a[-1]
        else:
            r = ''
            for i in range(len(a)):
                r += d[i] + a[i]
            if len(d) > len(a):
                r += d[-1]
        return r


if __name__ == '__main__':
    print(Solution().reformat('ab13'))
