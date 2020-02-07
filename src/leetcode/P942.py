class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        ret = []
        lo, hi = 0, n
        for i in range(n):
            if S[i] == 'I':
                ret.append(lo)
                lo += 1
            else:
                ret.append(hi)
                hi -= 1
        return ret + [hi]


if __name__ == '__main__':
    print(Solution().diStringMatch('IDID'))
