class Solution:
    def checkStraightLine(self, coordinates):
        n = len(coordinates)
        if n <= 2:
            return True
        k = None
        if coordinates[0][0] - coordinates[1][0] != 0:
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, n):
            for j in range(i + 1, n):
                t = None
                if coordinates[i][0] - coordinates[j][0] != 0:
                    t = (coordinates[i][1] - coordinates[j][1]) / (coordinates[i][0] - coordinates[j][0])
                if t != k:
                    return False
        return True
