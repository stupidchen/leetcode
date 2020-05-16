import math


class Solution:
    def simplifiedFractions(self, n: int):
        r = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1:
                    r.append('{}/{}'.format(i, j))
        return r


if __name__ == '__main__':
    print(Solution().simplifiedFractions(100))
