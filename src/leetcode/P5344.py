class Solution:
    def smallerNumbersThanCurrent(self, nums):
        f = [0] * 101
        for num in nums:
            f[num] += 1

        r = []
        for num in nums:
            t = 0
            for i in range(num):
                t += f[i]
            r.append(t)
        return r


# For test only
SI = (([8, 1, 2, 2, 3],),)
SO = ([4, 0, 1, 1, 3],)
TM = 'smallerNumbersThanCurrent'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
