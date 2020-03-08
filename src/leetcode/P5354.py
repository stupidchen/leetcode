class Solution:
    def numOfMinutes(self, n, headID, manager, informTime) -> int:
        f = [-1] * n

        def solve(node):
            if f[node] != -1:
                return f[node]

            if manager[node] == -1:
                f[node] = 0
                return 0

            f[node] = solve(manager[node]) + informTime[manager[node]]
            return f[node]

        r = 0
        for i in range(n):
            r = max(r, solve(i))
        return r


if __name__ == '__main__':
    print(Solution().numOfMinutes(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                                  informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
