D = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1),
}


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        d = {(x, y)}
        for p in path:
            dx, dy = D[p]
            x += dx
            y += dy
            if (x, y) in d:
                return True
            d.add((x, y))
        return False


if __name__ == '__main__':
    print(Solution().isPathCrossing('NES'))
    print(Solution().isPathCrossing('NESWW'))
