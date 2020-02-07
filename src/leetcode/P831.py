class Solution:
    def maskPII(self, S):
        if S.find('@') >= 0:
            s = S.lower()
            t = s.split('@')
            c1 = t[0][0]
            c2 = t[0][len(t[0]) - 1]
            ret = c1 + '*****' + c2 + '@' + t[1]
            return ret
        else:
            s = ''
            for c in S:
                if c >= '0' and c <= '9':
                    s += c
            if len(s) == 10:
                ret = '***-***-' + s[-4:]
            else:
                t = len(s) - 10
                ret = '+'
                for i in range(t):
                    ret += '*'
                ret += '-***-***-' + s[-4:]
            return ret

