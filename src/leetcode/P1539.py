class Solution:
    def findKthPositive(self, arr, k: int):
        r = 0
        for i in range(k):
            r += 1
            while r in arr:
                r += 1
        return r
