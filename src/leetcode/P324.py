from collections import deque
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = sorted(nums)
        m = n >> 1
        if n & 1 == 0:
            h1, h2 = deque(a[:m]), deque(a[m:])
        else:
            h1, h2 = deque(a[:m + 1]), deque(a[m + 1:])
        nums.clear()
        while h1 or h2:
            if h1:
                nums.append(h1.pop())
            if h2:
                nums.append(h2.pop())


if __name__ == '__main__':
    a = [1, 5, 1, 1, 6, 4]
    Solution().wiggleSort(a)
    print(a)
