from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        n = len(nums)

        def find(x, s):
            if x == n:
                if len(s) >= 2:
                    ret.add(tuple(s))
                return

            num = nums[x]
            if s and num >= s[-1] or not s:
                find(x + 1, s + [num])
            find(x + 1, s)

        find(0, [])
        return list(ret)


if __name__ == '__main__':
    print(Solution().findSubsequences([1] * 15))
