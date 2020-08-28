from math import floor


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r = sum([rand7() for i in range(10)])
        return r % 10 + 1
