class Solution:
    def isNStraightHand(self, hand, W):
        n = len(hand)
        if n % W != 0 or n == 0:
            return False
        if W == 1:
            return True

        hand = sorted(hand)
        f = [0] * n
        g = [0] * n
        g[0] = 1
        v = [False] * n
        c = 0
        last = 0
        r = 0
        for i in range(1, n):
            t = 0
            if hand[i] - hand[last] > 0:
                last = i - 1
            for j in range(last, 0, -1):
                if hand[j] + 1 == hand[i] and j > last:
                    last = j
                if hand[j] + 1 == hand[i] and g[j] < W and not v[j]:
                    t = j
                    break
                if hand[i] - hand[j] > 1:
                    break

            if hand[t] == hand[i] - 1 and g[t] < W and not v[t]:
                f[i] = f[t]
                g[i] = g[t] + 1
                v[t] = True
            else:
                c += 1
                f[i] = c
                g[i] = 1

            if g[i] == W:
                r += W

        return r == n


if __name__ == '__main__':
    s = Solution()
    print(s.isNStraightHand([1,2,3,1,2,3], 3))
