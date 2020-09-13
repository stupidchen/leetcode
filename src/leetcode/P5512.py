class Solution:
    def unhappyFriends(self, n: int, preferences, pairs):
        d = {}
        for x, y in pairs:
            d[x] = y
            d[y] = x

        r = 0
        for i in range(n):
            x, y = i, d[i]
            for u in preferences[x]:
                if u == y:
                    break
                v = d[u]
                f = False
                for j in range(len(preferences[u])):
                    if preferences[u][j] == v:
                        break
                    if preferences[u][j] == x:
                        r += 1
                        f = True
                        break
                if f:
                    break
        return r


if __name__ == '__main__':
    print(Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))
