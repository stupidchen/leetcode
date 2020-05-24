class Solution:
    def maxDotProduct(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        f = [[0] * (m + 1) for i in range(n + 1)]

        if (all([num >= 0 for num in nums1]) and all([num <= 0 for num in nums2])) or (all([num <= 0 for num in nums1]) and all([num >= 0 for num in nums2])):
            r = nums1[0] * nums2[0]
            for i in range(n):
                for j in range(m):
                    r = max(r, nums1[i] * nums2[j])
            return r

        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(nums1[i] * nums2[j] + f[i][j], max(f[i + 1][j], f[i][j + 1]))
        return f[n][m]


if __name__ == '__main__':
    print(Solution().maxDotProduct([-3, -8, 3, -10, 1, 3, 9],
                                   [9, 2, 3, 7, -9, 1, -8, 5, -1, -1]
                                   ))
