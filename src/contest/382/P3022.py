from functools import reduce
from typing import List


def lowest_bit(x):
    return x ^ (x & (x - 1))


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        while (next_num := (max_num - lowest_bit(max_num))) > 0:
            max_num = next_num

        bits = []
        while max_num > 0:
            bits.append(max_num)
            max_num = max_num >> 1

        def operations(target):
            ret = 0
            and_result = 0
            for i, num in enumerate(nums):
                if and_result != 0:
                    and_result &= (num & target)
                    ret += 1
                else:
                    if num & target > 0:
                        and_result = num & target

            if and_result != 0:
                ret += 1
            return ret

        current = 0
        full = reduce(lambda x, y: x | y, nums)
        for bit in bits:
            if full | bit == full and operations(current + bit) <= k:
                current += bit

        res = full - current
        return res


if __name__ == '__main__':
    r = Solution().minOrAfterOperations([56, 46, 45, 27, 3, 12], 4)
    print(r)
