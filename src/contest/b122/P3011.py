import math
from collections import Counter
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bit_nums = []
        for num in nums:
            bit_nums.append(Counter(bin(num)).get('1', 0))

        last = -1
        last_max = -1
        nums.append(max(nums) + 1)
        bit_nums.append(-2)
        min_num = math.inf
        max_num = -math.inf
        for num, bit_num in zip(nums, bit_nums):
            if last == -1:
                last = bit_num
                min_num = max_num = num
            elif last != bit_num:
                if min_num <= last_max:
                    return False
                last_max = max_num
                min_num = max_num = num
                last = bit_num
            else:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
        return True


if __name__ == '__main__':
    r = Solution().canSortArray(nums=[3, 16, 8, 4, 2])
    print(r)
