from heapq import heappush, heappop


class Solution:
    def eatenApples(self, apples, days):
        n = len(apples)
        m = 0
        for i, v in enumerate(days):
            m = max(i + v, m)

        h = []
        r = 0
        for i in range(m):
            if i < n:
                if apples[i] != 0:
                    heappush(h, [i + days[i], apples[i]])

            while h and (h[0][0] <= i or h[0][1] == 0):
                heappop(h)

            if h:
                r += 1
                h[0][1] -= 1
        return r


if __name__ == '__main__':
    print(Solution().eatenApples(apples=[1, 2, 3, 5, 2], days=[3, 2, 1, 4, 2]))
    print(Solution().eatenApples(apples=[7, 0, 0, 0, 0], days=[10, 0, 0, 0, 0]))
