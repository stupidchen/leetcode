class Solution:
    def peakIndexInMountainArray(self, A):
        last = -1
        for i in range(len(A)):
            if A[i] < last:
                return i - 1
            last = A[i]
        return len(A) - 1