class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        p = [-1] * n
        for edge in edges:
            x, y = edge
            p[y] = x

        f = [0] * n
        for i in reversed(range(n)):
            if p[i] != -1 and hasApple[i]:
                f[p[i]] += f[i] + 2
                hasApple[p[i]] = True
        return f[0]


if __name__ == '__main__':
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                             hasApple=[False, False, True, False, True, True, False]))

    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                             hasApple=[False, False, True, False, False, True, False]))
