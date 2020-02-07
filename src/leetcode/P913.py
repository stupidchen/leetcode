class Solution:
    f = []

    g = []

    def solve(self, x, y, z):
        f = self.f
        g = self.g
        if f[x][y][z] != -1:
            return f[x][y][z]
        f[x][y][z] = -2
        p = False
        if z == 0:
            d = False
            for v in g[x]:
                t = self.solve(v, y, 1 - z)
                if t == 1:
                    f[x][y][z] = 1
                    break
                if t == 0:
                    d = True
                if t == -2:
                    p = True
            if f[x][y][z] == -2 and d:
                f[x][y][z] = 0
            if f[x][y][z] == -2 and not p:
                f[x][y][z] = 2
        else:
            d = False
            for v in g[y]:
                if v != 0:
                    t = self.solve(x, v, 1 - z)
                    if t == 2:
                        f[x][y][z] = 2
                        break
                    if t == 0:
                        d = True
                    if t == -2:
                        p = True
            if f[x][y][z] == -2 and d:
                f[x][y][z] = 0
            if f[x][y][z] == -2 and not p:
                f[x][y][z] = 1
        return f[x][y][z]

    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        self.g = graph
        self.f = []
        for i in range(n):
            t = []
            for j in range(n):
                t.append([-1, -1])
            self.f.append(t)
        f = self.f
        for i in range(n):
            if i != 0:
                f[i][i][0] = 2
                f[i][i][1] = 2
                f[0][i][0] = 1
                f[0][i][1] = 1
        self.solve(1, 2, 0)
        return f[1][2][0]


if __name__ == '__main__':
    print(Solution().catMouseGame(
        [[3, 4, 6, 7, 9, 15, 16, 18], [4, 5, 8, 19], [4, 5, 6, 7, 9, 18], [0, 10, 11, 15], [0, 1, 2, 6, 10, 12, 14, 16],
         [1, 2, 7, 9, 15, 17, 18], [0, 2, 4, 7, 9, 10, 11, 12, 13, 14, 15, 17, 19], [0, 2, 5, 6, 9, 16, 17],
         [1, 9, 14, 15, 16, 19], [0, 2, 5, 6, 7, 8, 10, 11, 13, 15, 16, 17, 18], [3, 4, 6, 9, 17, 18],
         [3, 6, 9, 12, 19], [4, 6, 11, 15, 17, 19], [6, 9, 15, 17, 18, 19], [4, 6, 8, 15, 19],
         [0, 3, 5, 6, 8, 9, 12, 13, 14, 16, 19], [0, 4, 7, 8, 9, 15, 17, 18, 19], [5, 6, 7, 9, 10, 12, 13, 16],
         [0, 2, 5, 9, 10, 13, 16], [1, 6, 8, 11, 12, 13, 14, 15, 16]]))
