from data_structure.fenwickTree import FenwickTree

M = 1000


class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        if n == 0:
            return []
        # Avoid the negative number
        nums = list(map(lambda x: x + M, nums))
        m = max(nums)
        t = FenwickTree(m + 2)
        r = []
        for num in reversed(nums):
            r.append(t.get(num - 1))
            t.update(num, 1)
        return list(reversed(r))


# For test only
SI = (([5, 2, 6, 1],),)
SO = ([2, 1, 1, 0],)
TM = 'countSmaller'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
