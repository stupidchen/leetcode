class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            m1, m2 = 0, 0
            for stone in stones:
                if stone > m1:
                    m2 = m1
                    m1 = stone
                elif stone > m2:
                    m2 = stone
            stones.remove(m1)
            stones.remove(m2)
            if m1 - m2 != 0:
                stones.append(m1 - m2)
        if len(stones) > 0:
            return stones[0]
        return 0


if __name__ == '__main__':
    print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
