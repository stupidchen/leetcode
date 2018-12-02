class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ret = ''
        A = [str(a) for a in A]
        rh, rm = -1, -1
        for i in range(4):
            for j in range(4):
                if i != j:
                    for k in range(4):
                        if k != i and k != j:
                            for t in range(4):
                                if t not in (i, j, k):
                                    h = A[i] + A[j]
                                    m = A[k] + A[t]
                                    ih, im = int(h), int(m)
                                    if 0 <= ih < 24 and 0 <= im < 60:
                                        if ih > rh or (ih == rh and im > rm):
                                            rh, rm = ih, im
                                            ret = h + ':' + m
        return ret

if __name__ == '__main__':
    print(Solution().largestTimeFromDigits([0,0,1,0]))
