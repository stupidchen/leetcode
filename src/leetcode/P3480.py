class RecentCounter:

    def __init__(self):
        self.data = [0]
        self.index = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.data.append(t)
        while t > self.data[self.index] + 3000:
            self.index += 1
        if self.index == 0:
            return len(self.data) - self.index - 1
        else:
            return len(self.data) - self.index



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)