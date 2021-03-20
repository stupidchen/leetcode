from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.d = defaultdict(lambda: defaultdict(lambda: [0, 0]))
        self.c = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.c[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        fs, ft = self.c[id]
        tn, ta = self.d[fs][stationName]
        self.d[fs][stationName] = [tn + 1, (tn * ta + t - ft) / (tn + 1)]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tn, ta = self.d[startStation][endStation]
        return ta
