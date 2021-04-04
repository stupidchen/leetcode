class Solution:
    def squareIsWhite(self, coordinates):
        return (int(coordinates[0]) + ord(coordinates[1])) & 1 == 1
