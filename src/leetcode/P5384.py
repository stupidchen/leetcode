class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        r = []
        for c in candies:
            if m - c <= extraCandies:
                r.append(True)
            else:
                r.append(False)
        return r


if __name__ == '__main__':
    print(Solution().kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
