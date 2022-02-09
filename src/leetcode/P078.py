from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = set()
        for i in range(1 << n):
            t = []
            for j in range(n):
                if i | (1 << j) == i:
                    t.append(nums[j])
            ret.add(tuple(t))
        return list(map(list, ret))
