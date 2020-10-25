class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        s = []
        for i in range(1, n + 1):
            if i * i <= n:
                s.append(i * i)

        f = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in s:
                if j > i:
                    break
                if not f[i - j]:
                    f[i] = True
                    break

        return f[n]
