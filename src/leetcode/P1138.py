BOARD = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

COORD = {}

for i, row in enumerate(BOARD):
    for j, c in enumerate(row):
        COORD[c] = (i, j)


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        r = ''
        x, y = 0, 0
        for c in target:
            tx, ty = COORD[c]
            dx, dy = tx - x, ty - y

            if dy < 0:
                r += 'L' * (-dy)
            if dx < 0:
                r += 'U' * (-dx)

            if dy > 0:
                r += 'R' * dy
            if dx > 0:
                r += 'D' * dx

            r += '!'
            x, y = tx, ty
        return r


if __name__ == '__main__':
    print(Solution().alphabetBoardPath('leet'))
