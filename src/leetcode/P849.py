class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        last = -1
        max_seg = 0
        for i in range(n):
            if seats[i] == 1:
                if last != -1:
                    if (i - last) >> 1 > max_seg:
                        max_seg = (i - last) >> 1
                else:
                    max_seg = i
                last = i
        if n - 1 - last > max_seg:
            max_seg = n - 1 - last
        return max_seg