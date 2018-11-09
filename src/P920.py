from functools import lru_cache

MODULO = 10 ** 9 + 7

class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return +(j == 0)
            ans = dp(i - 1, j - 1) * (N - j + 1) + dp(i - 1, j) * max(j - K, 0)
            return ans % MODULO
        return dp(L, N)
