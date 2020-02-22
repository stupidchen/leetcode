M = 20000


def last(x):
    return x ^ (x & (x - 1))


def key(x):
    b = 0
    t = x
    while x > 0:
        x -= last(x)
        b += 1
    return M * b + t


class Solution:
    def sortByBits(self, arr):
        arr = sorted(arr, key=key)
        return arr


# For test only
SI = (([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],), ([10, 100, 1000, 10000],))
SO = ([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], [10, 100, 10000, 1000])
TM = 'sortByBits'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
