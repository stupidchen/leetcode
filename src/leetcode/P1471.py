class Solution:
    def getStrongest(self, arr, k):
        arr = sorted(arr)
        m = arr[(len(arr) - 1) >> 1]
        r = sorted(arr, key=lambda x: (-abs(x - m), -x))
        return r[:k]
