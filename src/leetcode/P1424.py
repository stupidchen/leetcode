from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums):
        d = defaultdict(lambda: [])
        n = len(nums)
        m = 0
        for i in range(n):
            for j in range(len(nums[i])):
                d[i + j].append(nums[i][j])
            m = max(m, i + len(nums[i]))
        r = []
        for i in range(m):
            r.extend(reversed(d[i]))
        return r


if __name__ == '__main__':
    print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
