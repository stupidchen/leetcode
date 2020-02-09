from collections import defaultdict


class Solution:
    def checkIfExist(self, arr):
        d = defaultdict(lambda: 0)
        for n in arr:
            d[n] += 1
        for n in arr:
            if n == 0 and d[n] > 1:
                return True
            elif n != 0 and n << 1 in d:
                return True
        return False


# For test only
SI = (([10, 2, 5, 3],), ([7, 1, 14, 11],), ([3, 1, 7, 11],))
SO = (True, True, False)
TM = 'checkIfExist'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
