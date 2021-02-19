class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        v = [False] * n
        t = []
        for i, c in enumerate(s):
            if c != '(' and c != ')':
                v[i] = True
            else:
                if c == '(':
                    t.append(i)
                else:
                    if t:
                        k = t.pop()
                        v[k] = True
                        v[i] = True
                    else:
                        continue
        r = ''
        for i in range(n):
            if v[i]:
                r += s[i]
        return r
