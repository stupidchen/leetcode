class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        i = 1
        while i < len(A) and A[i] > A[i - 1]:
            i += 1
        if i == 1 or i == len(A):
            return False
        i -= 1
        while i < len(A) - 1 and A[i] > A[i + 1]:
            i += 1
        if i < len(A) - 1:
            return False
        return True


if __name__ == '__main__':
    print(Solution().validMountainArray([1, 2, 1]))
