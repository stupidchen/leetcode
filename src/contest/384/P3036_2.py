from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        origin = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                origin[i] = 1
            elif nums[i + 1] < nums[i]:
                origin[i] = -1

        f = [0] * m
        matched = 0
        for i in range(1, m):
            while matched > 0 and pattern[matched] != pattern[i]:
                matched = f[matched - 1]
            if pattern[matched] == pattern[i]:
                matched += 1
            f[i] = matched

        res = 0
        matched = 0
        for i in range(n - 1):
            while matched > 0 and pattern[matched] != origin[i]:
                matched = f[matched - 1]
            if pattern[matched] == origin[i]:
                matched += 1
            if matched == m:
                res += 1
                matched = f[matched - 1]
        return res


if __name__ == '__main__':
    r = Solution().countMatchingSubarrays(nums=[1, 2, 3, 4, 5, 6], pattern=[1, 1])
    print(r)

