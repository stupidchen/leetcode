class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        i = 0
        while i < len(S):
            if i < len(S) - 1 and S[i] == '(' and S[i + 1] == ')':
                i += 1
                S = S[: i] + '1' + S[i:]
            i += 1
        S = '(' + S + ')'
        s = []
        for c in S:
            if c == '(':
                s.append(c)
            if c == '1':
                s.append(-1)
            if c == ')':
                tc = s.pop()
                t = 0
                while tc != '(':
                    if tc != -1:
                        t += tc << 1
                    else:
                        t += 1
                    tc = s.pop()
                s.append(t)
        ret = s[0] >> 1
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.scoreOfParentheses('(()(()))'))
