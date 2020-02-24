import collections


def compare(x, y):
    lx, ly = len(x), len(y)
    if lx > ly:
        return 1
    if lx < ly:
        return -1
    return -1


class Solution:
    def largestMultipleOfThree(self, digits):
        d = dict(collections.Counter(digits))
        for i in range(10):
            if i not in d:
                d[i] = 0
        f = [['', '', ''], ['', '', '']]
        t = 0
        for i in range(9, -1, -1):
            if i % 3 != 0 and d[i] != 0:
                s = str(i)
                m = i % 3
                for j in range(d[i]):
                    t = 1 - t
                    for o in range(3):
                        f[t][o] = f[1 - t][o]
                    for k in range(3):
                        if (f[1 - t][k] != '' or k == 0) and compare(f[1 - t][k] + s, f[t][(k + m) % 3]) > 0:
                            f[t][(k + m) % 3] = f[1 - t][k] + s
        t = dict(collections.Counter(f[t][0]))
        for i in range(10):
            s = str(i)
            if i % 3 == 0:
                t[s] = d[i]
            if s not in t:
                t[s] = 0
        r = ''
        for i in reversed(range(10)):
            s = str(i)
            r += s * t[s]
        if r != '' and r[0] == '0':
            r = '0'
        return r


if __name__ == '__main__':
    print(Solution().largestMultipleOfThree([1, 1, 1, 2]))
    print(Solution().largestMultipleOfThree([8, 1, 9]))
    print(Solution().largestMultipleOfThree([8, 6, 7, 1, 0]))
    print(Solution().largestMultipleOfThree([1]))
    print(Solution().largestMultipleOfThree([0, 0, 0, 0, 0, 0]))
