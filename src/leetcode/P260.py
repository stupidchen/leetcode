from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = reduce(lambda x, y: x ^ y, nums, 0)
        d = tmp & -tmp
        ret = [0, 0]
        for num in nums:
            ret[(num & d) == 0] ^= num
        return ret


if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 3, 4, 5, 5]))
