class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = 0
        r = 0
        ret = 0
        for s in S:
            if s == '(':
                l += 1
            else:
                r += 1
            if l < r:
                ret += 1
                r -= 1
        if l > r:
            ret += l - r
        return ret


if __name__ == '__main__':
    print(Solution().minAddToMakeValid('(()())'))
