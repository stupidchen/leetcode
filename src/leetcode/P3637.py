class Solution:
    def numberOfSteps(self, num: int) -> int:
        r = 0
        while num != 0:
            if num & 1 == 1:
                num -= 1
            else:
                num = num >> 1
            r += 1
        return r
