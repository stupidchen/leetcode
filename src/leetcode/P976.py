class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = sorted(A)
        n = len(a)
        ret = 0
        t = n - 1
        for i in reversed(range(1, n - 1)):
            while a[i] + a[i - 1] <= a[t] and t > i:
                t -= 1
            if t > i:
                ret = a[i] + a[i - 1] + a[t]
                break
        return ret


if __name__ == '__main__':
    print(Solution().largestPerimeter([1, 2, 1, 1]))
