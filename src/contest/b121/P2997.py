from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        for num in nums:
            b = bin(num)
            for i, bit in enumerate(reversed(b[2:])):
                bit = int(bit)
                counter[i] += bit

        b = bin(k)[2:]
        res = 0
        for i, bit in enumerate(reversed(b)):
            bit = int(bit)
            if bit != (counter[i] & 1):
                res += 1
            counter[i] = 0
        for v in counter.values():
            if v & 1 != 0:
                res += 1
        return res


if __name__ == '__main__':
    r = Solution().minOperations(nums=[2, 0, 2, 0], k=0)
    print(r)
