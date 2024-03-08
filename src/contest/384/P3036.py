from typing import List

MODULO = 10 ** 6 + 7
BASE = 11


def rolling_hash(s):
    res = 0
    for c in s:
        res = (res * BASE + c) % MODULO
    return res


def update_hash(old, char_in, char_out, power):
    return ((old - char_out * power) * BASE + char_in) % MODULO


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        origin = [1] * (n - 1)
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                origin[i] = 2
            elif nums[i + 1] < nums[i]:
                origin[i] = 0

        for i, p in enumerate(pattern):
            pattern[i] = p + 1

        pattern_hash = rolling_hash(pattern)
        origin_hash = rolling_hash(origin[:m])
        res = 1 if pattern_hash == origin_hash else 0
        power = 1
        for i in range(m - 1):
            power = (power * BASE) % MODULO
        for i in range(m, n - 1):
            origin_hash = update_hash(origin_hash, origin[i], origin[i - m], power)
            if origin_hash == pattern_hash:
                res += 1
        return res


if __name__ == '__main__':
    r = Solution().countMatchingSubarrays(nums=[1, 2, 3, 4, 5, 6], pattern=[1, 1])
    print(r)
