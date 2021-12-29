class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        r = set()

        def dfs(x, y):
            if y:
                r.add(y)
            if not x:
                return
            for i in range(len(x)):
                dfs(x[:i] + x[i + 1:], y + x[i])

        dfs(tiles, [])
        return len(r)
