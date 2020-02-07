class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        ret = []
        for i in range(n):
            t, p = 0, -1
            for j in range(n - i):
                if A[j] > t:
                    t, p = A[j], j
            if p == n - i - 1:
                continue

            if p != 0:
                ret.append(p + 1)
            ret.append(n - i)

            A = list(reversed(A[:p+1])) + A[p+1:]
            A = list(reversed(A[:n-i])) + A[n-i:]

        return ret


if __name__ == '__main__':
    print(Solution().pancakeSort([1, 2, 3]))
