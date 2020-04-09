def real_str(x):
    r = ''
    for c in x:
        if c == '#':
            r = r[:-1]
        else:
            r += c
    return r

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return real_str(S) == real_str(T)
