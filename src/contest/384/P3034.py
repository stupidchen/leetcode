from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        res = 0
        for i in range(n - m):
            matched = True
            for j in range(m):
                p = 0
                if nums[i + j + 1] > nums[i + j]:
                    p = 1
                elif nums[i + j + 1] < nums[i + j]:
                    p = -1
                if pattern[j] != p:
                    matched = False
                    break
            if matched:
                res += 1
        return res


if __name__ == '__main__':
    r = Solution().countMatchingSubarrays([1, 2], [1, 1])
    print(r)
