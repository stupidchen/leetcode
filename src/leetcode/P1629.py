class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        t = 0
        m = 0
        r = ''
        for i, c in enumerate(keysPressed):
            d = releaseTimes[i] - t
            if d > m or (d == m and c > r):
                m = releaseTimes[i] - t
                r = c
            t = releaseTimes[i]
        return r


if __name__ == '__main__':
    print(Solution().slowestKey([9, 29, 49, 50], "cbcd"))
