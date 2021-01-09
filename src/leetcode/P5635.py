class Solution:
    def constructDistancedSequence(self, n):
        m = (n << 1) - 1
        t = [0] * m
        v = [False] * (n + 1)
        c = [False]

        def find(x):
            if x >= m:
                c[0] = True
                return

            if t[x] == 0:
                for i in reversed(range(2, n + 1)):
                    if x + i < m and t[x + i] == 0 and not v[i]:
                        v[i] = True
                        t[x] = t[x + i] = i
                        find(x + 1)
                        if c[0]:
                            return
                        t[x] = t[x + i] = 0
                        v[i] = False
                if not v[1]:
                    v[1] = True
                    t[x] = 1
                    find(x + 1)
                    if c[0]:
                        return
                    t[x] = 0
                    v[1] = False
            else:
                find(x + 1)
                if c[0]:
                    return

        find(0)

        return t


if __name__ == '__main__':
    print(Solution().constructDistancedSequence(20))
