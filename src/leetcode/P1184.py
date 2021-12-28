from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = sum(distance)
        if start > destination:
            start, destination = destination, start
        r = 0
        for i in range(start, destination):
            r += distance[i]
        r = min(r, s - r)
        return r
