from collections import defaultdict
from functools import lru_cache


class Solution:
    ret = 0

    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        self.ret = 1
        b = [0] * n
        d = defaultdict(lambda: [])

        @lru_cache(maxsize=None)
        def solve(i, odd):
            if odd:
                b[i] = 1
            if i == 0:
                return
            if odd:
                j = i - 1
                t = 100001
                while j >= 0 and A[j] > A[i]:
                    if A[j] < t:
                        solve(j, False)
                    t = min(A[j], t)
                    j -= 1

            if not odd:
                j = i - 1
                t = -1
                while j >= 0 and A[j] < A[i]:
                    if A[j] > t:
                        solve(j, True)
                    t = max(A[j], t)
                    j -= 1

        solve(n - 1, True)
        solve(n - 1, False)
        return sum(b)

if __name__ == '__main__':
    print(Solution().oddEvenJumps([1,2,3,2,1,4,4,5]))
