from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        c = 0
        ret = 0
        diff = []
        for num in nums:
            if num ^ k > num:
                c += 1
            diff.append(abs((num ^ k) - num))
            ret += max(num ^ k, num)
        if c & 1 == 0:
            return ret
        else:
            ret = ret - min(diff)
            return ret


if __name__ == '__main__':
    # r = Solution().maximumValueSum(nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]])
    r = Solution().maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]])
    print(r)
