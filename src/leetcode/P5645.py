class Solution:
    def largestAltitude(self, gain):
        r = 0
        t = 0
        for g in gain:
            t += g
            r = max(t, r)
        return r