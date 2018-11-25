class Solution:
    def can_do(self, t, p, m):
        l = 0
        r = len(t) - 1
        for i in range((len(t) - m) >> 1):
            if p - t[l] >= 0:
                p = p - t[l] + t[r]
                l += 1
                r -= 1
                if l >= r:
                    break
            else:
                return False
        for i in range(l, r + 1):
            if p - t[i] >= 0:
                p -= t[i]
            else:
                return i - l >= m
        return r + 1 - l >= m

    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        t = sorted(tokens)
        l = 0
        r = len(tokens)
        ret = 0
        while l <= r:
            mid = (l + r) >> 1
            if self.can_do(t, P, mid):
                l = mid + 1
                ret = mid
            else:
                r = mid - 1
        return ret


if __name__ == '__main__':
    print(Solution().bagOfTokensScore([100,  900], 1000))
