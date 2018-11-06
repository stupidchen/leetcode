FROM = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4], [4, 6]]

MODULO = 10 ** 9 + 7


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = [1] * 10
        if N == 0:
            return 0
        if N == 1:
            return 10
        for i in range(1, N):
            t = [0] * 10
            for j in range(10):
                for k in FROM[j]:
                    t[j] = (t[j] + f[k]) % MODULO
            f = t
        ret = 0
        for i in range(10):
            ret = (ret + f[i]) % MODULO
        return ret


if __name__ == '__main__':
    print(Solution().knightDialer(5000))
