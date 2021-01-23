class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        m = n.bit_length()
        s = []
        for i in range(m):
            t = 0
            for j in range(1, n + 1):
                if j | (1 << i) != j:
                    t += 1
            s.append(t)

        f = 0
        for i in range(m):
            b = 0
            c = 1
            for e in encoded:
                t = 0
                if e | (1 << i) == e:
                    t = 1
                b = b ^ t
                if b == 0:
                    c += 1
            if c != s[i]:
                f += 1 << i

        r = [f]
        for e in encoded:
            r.append(r[-1] ^ e)
        return r


if __name__ == '__main__':
    print(Solution().decode([6, 5, 4, 6]))
