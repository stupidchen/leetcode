class Solution:
    def can(self, piles, H, K):
        h = 0
        for p in piles:
            h += p // K
            if p % K != 0:
                h += 1
            if h > H:
                return False
        return True

    def minEatingSpeed(self, piles, H):
        r = 0
        for p in piles:
            if p > r:
                r = p
        n = len(piles)
        if n > H:
            return -1
        l = 1
        ret = r
        while l <= r:
            mid = (l + r) >> 1
            if self.can(piles, H, mid):
                ret = mid
                r = mid - 1
            else:
                l = mid + 1
        return ret
