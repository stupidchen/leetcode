from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        f = [0] * (n + 1)
        d = defaultdict(lambda: 0)
        for i in range(n):
            f[i + 1] = f[i] + A[i]
        for i in range(n + 1):
            d[f[i] % K] += 1

        return sum([(v * (v - 1)) >> 1 for v in d.values()])


if __name__ == '__main__':
    print(Solution().subarraysDivByK([-1, -2, -3, -4], 5))
