class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_num = A[0]
        min_num = A[0]
        for num in A:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
        return max((max_num - min_num) - (K << 1), 0)
