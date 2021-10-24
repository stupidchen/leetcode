from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        def solve(l, r, return_max=True):
            if l + 1 == r:
                nums[l], str(nums[l])
            s = '/'.join(str(num) for num in nums[l: r])
            m = eval(s)
            for i in range(l + 1, r):
                ml, sl = solve(l, i)
                mr, sr = solve(i, r, return_max=False)
                t = ml / mr
                v = t > m if return_max else t < m
                if v or (t == m and len(sl + sr) + 3 < len(s)):
                    m = t
                    s = f'{sl}/({sr})'
            return m, s

        return solve(0, len(nums))[1]


if __name__ == '__main__':
    print(Solution().optimalDivision([1000, 100, 10, 2]))
    print(Solution().optimalDivision([2, 3, 4]))
    print(Solution().optimalDivision([2]))
