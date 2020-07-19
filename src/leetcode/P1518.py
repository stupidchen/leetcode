class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        r = 0
        k = numBottles
        e = 0
        while k != 0:
            r += k
            t = k
            k = (k + e) // numExchange
            e = (t + e) % numExchange
        return r


if __name__ == '__main__':
    print(Solution().numWaterBottles(15, 4))
