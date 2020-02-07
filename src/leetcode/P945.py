class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = sorted(A)
        ret = 0
        for i in range(1, len(A)):
            if a[i] <= a[i - 1]:
                t = a[i - 1] - a[i] + 1
                ret += t
                a[i] = a[i - 1] + 1
        return ret

if __name__ == '__main__':
    print(Solution().minIncrementForUnique([3,1]))
