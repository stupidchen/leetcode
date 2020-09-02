class Solution:
    def getLastMoment(self, n, left, right):
        r = 0
        for ll in left:
            r = max(ll, r)
        for rr in right:
            r = max(n - rr, r)
        return r


if __name__ == '__main__':
    print(Solution().getLastMoment(20, [4, 7, 15], [9, 3, 13, 10]))
    print(Solution().getLastMoment(n=7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]))
    print(Solution().getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]))
    print(Solution().getLastMoment(n=4, left=[4, 3], right=[0, 1]))
