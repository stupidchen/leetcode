class Solution:
    def carPooling(self, trips, capacity):
        events = []
        for num, start, end in trips:
            events.append((start, num))
            events.append((end, -num))

        events = sorted(events)
        t = capacity
        for time, num in events:
            t -= num
            if t < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
