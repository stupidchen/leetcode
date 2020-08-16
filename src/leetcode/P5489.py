class Solution:
    def maxDistance(self, position, m):
        position.sort()
        n = len(position)

        def can(x):
            t = 0
            for i in range(m - 1):
                k = -1
                for j in range(t + 1, n):
                    if position[j] - position[t] >= x:
                        k = j
                        break
                if k != -1:
                    t = k
                else:
                    return False

            return True

        l, r = 0, position[-1] - position[0]
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
    print(Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))
