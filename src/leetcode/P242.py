class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        for c in t:
            d[c] = d.setdefault(c, 0) - 1
        for v in d.values():
            if v != 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram('rat', 'art'))
