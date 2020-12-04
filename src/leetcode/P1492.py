class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        t = 0
        for i in range(1, n + 1):
            if n % i == 0:
                t += 1
            if t == k:
                return i
        return -1
