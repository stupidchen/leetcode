from collections import defaultdict


class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        def solve(a, b):
            d = defaultdict(lambda: 0)
            for num in a:
                d[num * num] += 1

            n = len(b)
            r = 0
            for i in range(n):
                for j in range(i + 1, n):
                    r += d[b[i] * b[j]]
            return r

        return solve(nums1, nums2) + solve(nums2, nums1)


if __name__ == '__main__':
    print(Solution().numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
