from math import sqrt, floor


class Solution:
    def constructRectangle(self, area):
        i = floor(sqrt(area))
        while area % i != 0:
            i -= 1
        return [i, area // i]
