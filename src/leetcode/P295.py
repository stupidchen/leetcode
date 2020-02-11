import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bh = []
        self.sh = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.bh) > len(self.sh):
            if self.bh and num < -self.bh[0]:
                t = -heapq.heappop(self.bh)
                heapq.heappush(self.bh, -num)
                heapq.heappush(self.sh, t)
            else:
                heapq.heappush(self.sh, num)
        else:
            if self.sh and num > self.sh[0]:
                t = heapq.heappop(self.sh)
                heapq.heappush(self.sh, num)
                heapq.heappush(self.bh, -t)
            else:
                heapq.heappush(self.bh, -num)

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.sh and not self.bh:
            return 0

        if len(self.sh) > len(self.bh):
            return self.sh[0]

        if len(self.sh) < len(self.bh):
            return -self.bh[0]

        return (self.sh[0] - self.bh[0]) / 2


# This kind of input is not supported by tester temporarily
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    obj.addNum(-3)
    obj.addNum(-4)
    obj.addNum(-5)
    obj.addNum(-6)
    print(obj.findMedian())
