class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)
        v = [(aliceValues[i], bobValues[i]) for i in range(n)]
        v = sorted(v, key=lambda x: -(x[0] + x[1]))
        a = b = 0
        for i in range(n):
            if i & 1 == 0:
                a += v[i][0]
            else:
                b += v[i][1]
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


if __name__ == '__main__':
    print(Solution().stoneGameVI(aliceValues=[2, 4, 3], bobValues=[1, 6, 7]))
    print(Solution().stoneGameVI(aliceValues=[1, 2], bobValues=[3, 1]))
    print(Solution().stoneGameVI(aliceValues=[1, 3], bobValues=[2, 1]))
