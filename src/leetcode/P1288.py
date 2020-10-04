class Solution:
    def removeCoveredIntervals(self, intervals):
        n = len(intervals)
        r = n
        for i in range(n):
            for j in range(n):
                if i != j and intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    r -= 1
                    break
        return r
