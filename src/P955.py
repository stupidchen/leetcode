class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n, m = len(A), len(A[0])
        ret = 0
        o = [0] * n
        for p in range(m):
            lex = True
            for i in range(1, n):
                if A[i][p] < A[i - 1][p] and o[i - 1] == o[i]:
                    lex = False
                    break
            if not lex:
                ret += 1
            else:
                c = False
                for i in range(1, n):
                    if o[i - 1] == o[i]:
                        if A[i][p] > A[i - 1][p]:
                            for j in range(i, n):
                                o[j] += 1
                            continue
                        if A[i][p] == A[i - 1][p]:
                            c = True
                if not c:
                    break
        return ret


if __name__ == '__main__':
    print(Solution().minDeletionSize(["uyx", "uya","wzb","wza"]))
