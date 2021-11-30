from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        t = 0
        for v, i in enumerate(nums):
            if s - i == t:
                return v
            s -= i
            t += i
        return -1


if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
