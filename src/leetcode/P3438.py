class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        ti = [intervals[i] + [i] for i in range(n)]
        si = sorted(ti, key=lambda i: i[0] * 10000000000 + i[1])
        ret = [-1] * n
        for k in range(n):
            i = si[k]
            l, r = k + 1, n - 1
            a = -1
            while l <= r:
                mid = (l + r) >> 1
                if si[mid][0] >= i[1]:
                    r = mid - 1
                    a = si[mid][2]
                else:
                    l = mid + 1
            ret[i[2]] = a
        return ret


if __name__ == '__main__':
    print(Solution().findRightInterval([[1, 2]]))
    print(Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]))
