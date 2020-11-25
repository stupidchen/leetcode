class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1

        s, r = 1, 1 % K
        while r != 0:
            r = (r * 10 + 1) % K
            s += 1
        return s
