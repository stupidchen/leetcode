from collections import Counter


class Solution:
    def maximumBinaryString(self, binary):
        z1 = 0
        t = 0
        for c in binary:
            if c == '1':
                z1 += 1
            else:
                break
            t += 1

        b = binary[t:]
        d = dict(Counter(b))
        c0 = c1 = 0
        if '0' in d:
            c0 = d['0']
        if '1' in d:
            c1 = d['1']

        r = z1 * '1' + (((c0 - 1) * '1' + '0') if c0 > 0 else '') + c1 * '1'
        if r < binary:
            r = binary
        return r


if __name__ == '__main__':
    print(Solution().maximumBinaryString('1100'))
