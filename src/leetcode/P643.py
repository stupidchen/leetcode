from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        r = s / k
        for i in range(k, len(nums)):
            s = s - nums[i - k] + nums[i]
            r = max(s / k, r)
        return r


if __name__ == '__main__':
    print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
