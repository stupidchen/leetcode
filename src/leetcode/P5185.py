class Solution:
    def threeConsecutiveOdds(self, arr):
        t = 0
        for a in arr:
            if a & 1 == 1:
                t += 1
                if t == 3:
                    return True
            else:
                t = 0
        return False
