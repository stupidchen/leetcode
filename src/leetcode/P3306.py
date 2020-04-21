# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, x: int, y: int):
        pass

    def dimensions(self):
        pass


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        x, y = 0, m - 1
        r = -1
        while x < n and y >= 0:
            t = binaryMatrix.get(x, y)
            if t == 0:
                x += 1
            else:
                r = y
                y -= 1

        return r
