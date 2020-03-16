class Solution:
    def minMoves(self, nums):
        m = min(nums)
        return sum(num - m for num in nums)


if __name__ == '__main__':
    print(Solution().minMoves([1, 2, 3]))
