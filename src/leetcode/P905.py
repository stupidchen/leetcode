class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for a in A:
            if (a & 1) == 1:
                odd.append(a)
            else:
                even.append(a)
        return even + odd
