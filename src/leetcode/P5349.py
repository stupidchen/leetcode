from collections import defaultdict


def reserved(s, l, r):
    return all(i not in s for i in range(l, r))


def solve(s):
    if reserved(s, 2, 10):
        return 2

    if reserved(s, 2, 6):
        return 1

    if reserved(s, 6, 10):
        return 1

    if reserved(s, 4, 8):
        return 1

    return 0


class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        d = defaultdict(lambda: [])
        for seat in reservedSeats:
            r, c = seat
            d[r].append(c)
        r = 0
        for s in d.values():
            r += solve(s)
        return r + (n - len(d.values())) * 2


if __name__ == '__main__':
    print(Solution().maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
