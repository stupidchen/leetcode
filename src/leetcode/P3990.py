class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ret = [0] * len(A)
        index = [0, 1]
        for a in A:
            ret[index[a & 1]] = a
            index[a & 1] += 2
        return ret
