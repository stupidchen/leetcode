class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        n = len(heights)
        a = []
        for i in range(1, n):
            t = heights[i] - heights[i - 1]
            if t > 0:
                a.append((t, i))
        a = sorted(a, key=lambda x: (-x[0], x[1]))
        m = len(a)

        def can(target):
            _ladders = ladders
            _bricks = bricks

            for i in range(m):
                if a[i][1] <= target:
                    if _ladders > 0:
                        _ladders -= 1
                    else:
                        if _bricks >= a[i][0]:
                            _bricks -= a[i][0]
                        else:
                            return False
            return True

        l = 0
        r = n - 1
        ret = 0
        while l <= r:
            mid = (l + r) >> 1
            if can(mid):
                l = mid + 1
                ret = mid
            else:
                r = mid - 1
        return ret


if __name__ == '__main__':
    print(Solution().furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
    print(Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
