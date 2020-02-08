class Solution:
    def numberOfSteps(self, num: int) -> int:
        r = 0
        while num != 0:
            if num & 1 == 1:
                num -= 1
            else:
                num = num >> 1
            r += 1
        return r


# For test only
SI = ((14,), (8,), (123,))
SO = (6, 4, 12)
TM = 'numberOfSteps'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
