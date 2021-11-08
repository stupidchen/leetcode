def query(s, x):
    t = []
    while s[x] != x:
        t.append(x)
        x = s[x]
    for i in t:
        s[i] = x
    return x


def merge(s, x, y):
    sx, sy = query(s, x), query(s, y)
    s[sy] = sx


class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        a = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    merge(a, i, j)
        s = set()
        for i in range(n):
            s.add(query(a, i))
        return len(s)
