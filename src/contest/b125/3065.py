from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len(list(filter(lambda x: x < k, nums)))

