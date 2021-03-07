class Solution:
    def minElements(self, nums, limit, goal):
        s = sum(nums)
        return (abs(goal - s) - 1) // limit + 1