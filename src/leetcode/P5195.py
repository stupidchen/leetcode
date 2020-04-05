class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        r = ''
        t = [[a, 'a'], [b, 'b'], [c, 'c']]
        l = None
        while 1:
            u = [0, '']
            for i in t:
                if i[1] != l and i[0] > u[0]:
                    u = i
            if u[0] == 0:
                break
            f = min(2, u[0])
            if max(t)[1] != u[1]:
                f = 1
            r += u[1] * f
            u[0] -= f
            l = u[1]

        return r


if __name__ == '__main__':
    print(Solution().longestDiverseString(0, 8, 11))
