from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=lambda x: int(x), reverse=True)
        return nums[k - 1]


if __name__ == '__main__':
    print(Solution().kthLargestNumber(['2' * 1000, '1' * 1000], 2))
