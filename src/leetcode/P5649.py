class Solution:
    def decode(self, encoded, first):
        r = [first]
        for e in encoded:
            r.append(r[-1] ^ e)
        return r
