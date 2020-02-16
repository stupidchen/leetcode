def invalid(a):
    return any(map(lambda x: x < 1, a))


def valid(a):
    return all(map(lambda x: x == 1, a))


def move(a):
    s, m = sum(a), max(a)
    for i in range(len(a)):
        if a[i] == m:
            a[i] -= (s - m)
            break


class Solution:
    def isPossible(self, target):
        if not target:
            return False
        while not valid(target):
            move(target)
            if invalid(target):
                return False

        return True


# For test only
SI = (([1, 1, 1, 2],),
      ([8, 5],),
      ([5, 3, 7],),
      ([9, 3, 5],))
SO = (False, True, False, True)
TM = 'isPossible'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
