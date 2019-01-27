from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(lambda: [])

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.d[key].append((timestamp, value))

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        values = self.d[key]
        if len(values) == 0:
            return ""
        l, r = 0, len(values) - 1
        ret = ""
        while l <= r:
            mid = (l + r)
            if values[mid][0] <= timestamp:
                l = mid + 1
                ret = values[mid][1]
            else:
                r = mid - 1
        return ret

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)