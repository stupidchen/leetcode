from math import floor, sqrt


def find(x):
    for i in reversed(range(1, floor(sqrt(x)) + 1)):
        if x % i == 0:
            return i, x // i, x // i - i


class Solution:
    def closestDivisors(self, num):
        x1, y1, d1 = find(num + 1)
        x2, y2, d2 = find(num + 2)
        if d1 < d2:
            return [x1, y1]
        else:
            return [x2, y2]


if __name__ == '__main__':
    print(Solution().closestDivisors(10 ** 9))
