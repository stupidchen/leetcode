class Solution:
    def stringShift(self, s, shift):
        i = 0
        n = len(s)
        for d, a in shift:
            if d == 0:
                i += a
                if i >= n:
                    i -= n
            if d == 1:
                i -= a
                if i < 0:
                    i += n
        return s[i:] + s[:i]


if __name__ == '__main__':
    print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))
