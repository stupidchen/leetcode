class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        si = sorted(intervals, key=lambda i: i[1])
        ret = 0
        r = si[0][1]
        for i in range(1, len(intervals)):
            interval = si[i]
            if interval[0] < r:
                ret += 1
            else:
                r = interval[1]
        return ret
