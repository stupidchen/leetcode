class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = 0
        s += ' '
        ret = 0
        for c in s:
            if c != ' ':
                word += 1
            else:
                ret += 1 if word != 0 else 0
                word = 0
        return ret


if __name__ == '__main__':
    print(Solution().countSegments("H"))
