class Solution:
    def intervalIntersection(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return []
        ai, bi = 0, 0
        ret = []
        if A[ai][0] < B[ai][0] or (A[ai][0] == B[ai][0] and A[ai][1] < B[bi][1]):
            l, r = A[ai][0], A[ai][1]
            ai += 1
        else:
            l, r = B[bi][0], B[bi][1]
            bi += 1

        while ai < len(A) or bi < len(B):
            t = None
            if ai < len(A):
                t = A[ai]
            if bi < len(B):
                if t is None or t[0] > B[bi][0] or (t[0] == B[bi][0] and t[1] > B[bi][1]):
                    t = B[bi]
                    bi += 1
                else:
                    ai += 1
            else:
                ai += 1

            if t[0] <= r:
                ret.append([t[0], min(r, t[1])])
            r = max(t[1], r)

        return ret
