class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.s = [0] * (self.n + 1)
        for i in range(self.n):
            self.s[i + 1] = self.s[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i = max(0, i)
        j = min(self.n - 1, j)
        return self.s[j + 1] - self.s[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)