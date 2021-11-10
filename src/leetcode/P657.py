class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for move in moves:
            if move == 'U':
                x -= 1
            if move == 'D':
                x += 1
            if move == 'L':
                y -= 1
            if move == 'R':
                y += 1
        if x == y == 0:
            return True
        return False


if __name__ == '__main__':
    print(Solution().judgeCircle("DURDLDRRLL"))
