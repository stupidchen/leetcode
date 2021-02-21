class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        x, y = X, Y
        ret = 0
        while x < y:
            ret += 1
            if y & 1 == 1:
                y += 1
            else:
                y = y >> 1
        ret += x - y

        return ret
