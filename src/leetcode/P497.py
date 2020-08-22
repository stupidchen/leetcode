import bisect
import random
from itertools import accumulate


class Solution:
    def __init__(self, rects):
        self.a = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.a = [i / sum(self.a) for i in accumulate(self.a)]
        self.r = rects

    def pick(self):
        d = random.random()
        t = bisect.bisect_left(self.a, d)
        x1, y1, x2, y2 = self.r[t]
        return random.randint(x1, x2), random.randint(y1, y2)


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == '__main__':
    o = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    print(o.pick())
    print(o.pick())
    print(o.pick())
    print(o.pick())
