class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        n = len(startTime)
        r = 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                r += 1
        return r


if __name__ == '__main__':
    print()