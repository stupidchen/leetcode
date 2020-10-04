class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        b = bin(n)[2:]
        r = ''
        ob = 0
        for i in range(len(b)):
            bit = int(b[i])
            if ob == 0:
                r += str(bit)
            else:
                r += str(1 - bit)
            if bit == 1:
                ob = 1 - ob
        return int(r, 2)
