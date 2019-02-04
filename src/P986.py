# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)


class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if len(A) == 0 or len(B) == 0:
            return []
        ai, bi = 0, 0
        ret = []
        if A[ai].start < B[ai].start or (A[ai].start == B[ai].start and A[ai].end < B[bi].end):
            l, r = A[ai].start, A[ai].end
            ai += 1
        else:
            l, r = B[bi].start, B[bi].end
            bi += 1

        while ai < len(A) or bi < len(B):
            t = None
            if ai < len(A):
                t = A[ai]
            if bi < len(B):
                if t is None or t.start > B[bi].start or (t.start == B[bi].start and t.end > B[bi].end):
                    t = B[bi]
                    bi += 1
                else:
                    ai += 1
            else:
                ai += 1

            if t.start <= r:
                ret.append(Interval(t.start, min(r, t.end)))
            r = max(t.end, r)

        return ret


if __name__ == '__main__':
    print([str(i) for i in Solution().intervalIntersection([Interval(0, 2), Interval(5, 10), Interval(13, 23), Interval(24, 25)],
                                                           [Interval(1, 5), Interval(8, 12), Interval(15, 24), Interval(25, 26)])])
