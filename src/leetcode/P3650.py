class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][-1]:
                l = 0
                r = m - 1
                while l <= r:
                    mid = (l + r) >> 1
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False
