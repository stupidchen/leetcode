class NumArray:

    def __init__(self, nums):
        n = len(nums)
        self.s = [0] * (n + 1)
        for i in range(n):
            self.s[i + 1] = self.s[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
