class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        c = ''
        for s in S:
            if s != '-':
                c += s.upper()

        n = len(c)
        r = c[:(n - 1) % K + 1]
        i = len(r)
        while i < n:
            r += '-' + c[i:i + K]
            i += K
        return r


# For test only
SI = (("5F3Z-2e-9-w", 4),
      ("2-5g-3-J", 2),)
SO = ("5F3Z-2E9W", "2-5G-3J")
TM = 'licenseKeyFormatting'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
