class Solution:
    def largeGroupPositions(self, S):
        s = S
        ret = []
        last = None
        t = 0
        f = 0
        for i in range(len(s)):
            c = s[i]
            if c != last:
                if t >= 3: 
                    ret.append([f, i - 1])
                t = 0
                f = i 
            t += 1
            last = c
            
        if t >= 3: 
            ret.append([f, len(s) - 1])
        return ret
