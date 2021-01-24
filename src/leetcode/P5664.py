class Solution:
    def minimumBoxes(self, n: int):
        t = 0
        m = 0
        i = 1
        while True:
            t += (i * (i + 1)) >> 1
            if t >= n:
                m = i
                break
            i += 1

        if t == n:
            return (m * (m + 1)) >> 1
        t -= (m * (m + 1)) >> 1
        m -= 1
        j = 1
        r = (m * (m + 1)) >> 1
        while True:
            r += 1
            t += j
            if t >= n:
                return r
            j += 1


if __name__ == '__main__':
    for i in range(20):
        print(Solution().minimumBoxes(i + 1))
