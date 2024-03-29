from collections import defaultdict


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)
        f = [0] * n
        m = max(obstacles)
        g = defaultdict(lambda: m + 1)
        g[0] = 0
        ret = []
        for i, v in enumerate(obstacles):
            l, r = 0, n
            while l <= r:
                mid = (l + r) >> 1
                if g[mid] <= v:
                    f[i] = mid + 1
                    l = mid + 1
                else:
                    r = mid - 1
            g[f[i]] = min(g[f[i]], v)
            ret.append(f[i])
        return ret


if __name__ == '__main__':
    print(Solution().longestObstacleCourseAtEachPosition([1, 2, 3, 2]))
