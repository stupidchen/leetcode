class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = abs((hour + minutes / 60) * 5 + - minutes) * 6
        return min(360 - a, a)


# For test only
SI = ((12, 30), (3, 30), (3, 15), (4, 50), (12, 0))
SO = (165, 75, 7.5, 155, 0)
TM = 'angleClock'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()

