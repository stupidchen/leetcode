MAXC = 10001


def query(s, x):
    t = []
    while s[x] != x:
        t.append(x)
        x = s[x]
    for i in t:
        s[i] = x
    return x


def merge(s, r, x, y):
    sx, sy = query(s, x), query(s, y)
    if sx != sy:
        if r[sx] > r[sy]:
            s[sy] = sx
            r[sx] = max(r[sy] + 1, r[sx])
        else:
            s[sx] = s[sy]
            r[sy] = max(r[sx] + 1, r[sy])


class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        s = [i for i in range(n)]
        r = [1] * n

        row = [-1] * MAXC
        col = [-1] * MAXC
        for i in range(n):
            if row[stones[i][0]] != -1:
                merge(s, r, row[stones[i][0]], i)
            else:
                row[stones[i][0]] = i
            if col[stones[i][1]] != -1:
                merge(s, r, col[stones[i][1]], i)
            else:
                col[stones[i][1]] = i

        ret = n
        for i in range(n):
            ret -= 1 if i == s[i] else 0

        return ret


if __name__ == '__main__':
    print(Solution().removeStones(
        [[0, 0], [0, 1], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]]))
    print(Solution().removeStones([[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]))
