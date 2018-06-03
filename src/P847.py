class Solution:
    def solve(self, c, s, v, f, t, graph):
        if not (f[v][c] == -1 or f[v][c] > s):
            return
        f[v][c] = s
        if v == t:
            return

        for i in graph[c]:
            next_v = v | (1 << i)
            self.solve(i, s + 1, next_v, f, t, graph)

    def shortestPathLength(self, graph):
        n = len(graph)
        if n == 0 or n == 1:
            return 0
        f = []
        for i in range(1 << n):
            f.append([-1] * n)
        for i in range(n):
            self.solve(i, 0, 1 << i, f, (1 << n) - 1, graph)

        ans = -1
        for i in range(n):
            if f[(1 << n) - 1][i] != -1 and (ans == -1 or f[(1 << n) - 1][i] < ans):
                ans = f[(1 << n) - 1][i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
