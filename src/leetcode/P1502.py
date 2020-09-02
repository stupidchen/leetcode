class Solution:
    def canMakeArithmeticProgression(self, arr):
        a = sorted(arr)
        d = a[1] - a[0]
        return all([a[i + 1] - a[i] == d for i in range(len(arr) - 1)])
