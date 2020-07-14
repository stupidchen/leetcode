class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs((hour + minutes / 60) * 5 + - minutes) * 6
        return min(360 - a, a)
