class Solution:
    def largestOverlap(self, A, B):
        an = len(A)
        am = len(A[0])
        bn = len(B)
        bm = len(B[0])
        r = 0
        for i in range(-bn, bn):
            for j in range(-bm, bm):
                k = 0
                for ti in range(an):
                    for tj in range(am):
                        if 0 <= ti + i < bn and 0 <= tj + j < bm and A[ti][tj] == B[ti + i][tj + j] == 1:
                            k += 1
                r = max(k, r)
        return r


if __name__ == '__main__':
    print(
        Solution().largestOverlap([[0, 0, 0, 0, 0],
                                   [0, 1, 0, 0, 0],
                                   [0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 1],
                                   [0, 1, 0, 0, 1]],
                                  [[1, 0, 1, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [0, 1, 1, 1, 1],
                                   [1, 0, 1, 1, 1]]))
