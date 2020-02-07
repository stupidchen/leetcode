class Solution:
    def binaryGap(self, N):
        l = -1
        i = 0
        ret = 0
        while N > 0:
            t = N & 1
            if t == 1:
                if l != -1:
                    if i - l > ret:
                        ret = i - l
                l = i
            i += 1
            N = N >> 1
        return ret

if __name__ == '__main__':
    print(Solution().binaryGap(128838383))