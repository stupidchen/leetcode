DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        n = len(instructions)
        x, y = 0, 0
        d = 0
        v = {(0, x, y)}
        for i in range(100000):
            t = instructions[i % n]
            if t == 'L':
                d = (d - 1) % 4
            elif t == 'R':
                d = (d + 1) % 4
            else:
                x, y = x + DX[d], y + DY[d]
            if (i % n + 1, x, y) in v:
                return True
            v.add((i % n + 1, x, y))

        return False


if __name__ == '__main__':
    print(Solution().isRobotBounded("LRRRRLLLRL"))
