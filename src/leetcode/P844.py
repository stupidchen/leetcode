class Solution:
    def getstr(self, str):
        ret = ''
        for c in str:
            if c == '#':
                if len(ret) > 0:
                    ret = ret[:-1]
            else:
                ret += c
        return ret

    def backspaceCompare(self, S, T):
        return self.getstr(S) == self.getstr(T)