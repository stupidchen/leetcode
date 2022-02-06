from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        nums.sort()
        p = {}
        for i in range(1, n):
            p[nums[i - 1]] = nums[i]
        s = min(nums)
        e = max(nums)
        p[e] = e + 1
        c = Counter(nums)
        m = n // k
        for i in range(m):
            for j in range(k):
                t = s + j
                c[t] -= 1
                if c[t] < 0:
                    return False
            while s <= e and c[s] == 0:
                s = p[s]
        return True


if __name__ == '__main__':
    print(Solution().isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))
