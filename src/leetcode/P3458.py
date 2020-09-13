class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)
        if n == 0:
            intervals.append(newInterval)
            return intervals
        i = -1
        if newInterval > intervals[-1]:
            i = n
        elif newInterval < intervals[0]:
            i = 0
        else:
            for i, interval in enumerate(intervals):
                if intervals[i - 1] <= newInterval <= intervals[i]:
                    break
        r = i
        while r < n:
            if newInterval[1] >= intervals[r][0]:
                r += 1
            else:
                break
        l = i - 1
        while l >= 0:
            if newInterval[0] <= intervals[l][1]:
                l -= 1
            else:
                break

        if r != i:
            newInterval[0] = min(newInterval[0], intervals[r - 1][0])
            newInterval[1] = max(newInterval[1], intervals[r - 1][1])

        if l + 1 != i:
            newInterval[0] = min(newInterval[0], intervals[l + 1][0])
            newInterval[1] = max(newInterval[1], intervals[l + 1][1])

        return intervals[:l + 1] + [newInterval] + intervals[r:]


if __name__ == '__main__':
    print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 6]))
