class Solution:
    def validUtf8(self, data):
        i, n = 0, len(data)
        while i < n:
            b = data[i] & 0xff
            if (b & 0xf8) >> 3  == 0x1e:
                r = i + 4
            elif (b & 0xf0) >> 4 == 0x0e:
                r = i + 3
            elif (b & 0xc0) >> 5 == 0x06:
                r = i + 2
            elif (b & 0x80) == 0:
                r = i + 1
            else:
                return False

            if r > n:
                return False
            for j in range(i + 1, r):
                if (data[j] & 0xc0) >> 6 != 0x02:
                    return False
            i = r
        return True

if __name__ == '__main__':
    print(Solution().validUtf8([235, 140, 4]))
