class Solution:
    def numTimesAllBlue(self, light):
        n = len(light)
        m, t = 0, 0
        r = 0
        for i in range(n):
            m = max(light[i], m)
            t += 1
            if m == t:
                r += 1

        return r


if __name__ == '__main__':
    print(Solution().numTimesAllBlue([2,1,4,3,6,5]))
