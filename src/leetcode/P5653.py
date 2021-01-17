from collections import Counter


class Solution:
    def countGoodRectangles(self, rectangles):
        c = Counter([min(l, w) for l, w in rectangles])
        return c[max(c.keys())]
