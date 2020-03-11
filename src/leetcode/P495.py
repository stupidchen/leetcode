class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        r = 0
        if len(timeSeries) == 0:
            return r
        l = timeSeries[0]
        for t in timeSeries:
            if t + duration >= l:
                r += min(duration + t - l, duration)
                l = t + duration
        return r


if __name__ == '__main__':
    print(Solution().findPoisonedDuration([1, 2], 2))
