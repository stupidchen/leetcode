class Solution:
    def findComplement(self, num: int) -> int:
        t = ((1 << num.bit_length()) - 1) ^ num
        return t


# For test only
SI = ((5,), (1,))
SO = (2, 0)
TM = 'findComplement'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
