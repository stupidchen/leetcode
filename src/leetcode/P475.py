class Solution:
    def findRadius(self, houses, heaters):
        n = len(houses)
        if n == 0:
            return 0

        houses = sorted(houses)
        heaters = sorted(heaters)

        def valid(r):
            c = 0
            for h in heaters:
                while c < n and abs(houses[c] - h) <= r:
                    c += 1
                if c == n:
                    return True
            return False

        l, r = 0, max(houses[-1], heaters[-1])
        while l < r:
            mid = (l + r) >> 1
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == '__main__':
    print(Solution().findRadius([1, 2, 3, 4], [1, 4]))
    print(Solution().findRadius([1, 5], [10]))
